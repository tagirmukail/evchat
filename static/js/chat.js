$(
    function() {
        var ws_sheme = window.location.protocol == "https:" ? "wss" : "ws";
        var ws_path = ws_sheme + "://" + window.location.host + "/chat/stream/";

        console.log("Connecting to " + ws_path);

        var socket = new ReconnectingWebSocket(ws_path);
        socket.debug = true;
        // Handle incoming messages
        socket.onmessage = function(message) {
            // Decode to JSON
            console.log("Got websocket message " + message.data);
            let data = JSON.parse(message.data);
            if (data.error) {
                alert(data.error);
                return;
            }

            // Handle joining
            if (data.join) {
                console.log("Joining room " + data.join);
                let roomdiv = $(
                    "<div class='room' id='room-" + data.join + "'>" +
                    "<h2>" + data.name + "</h2>" +
                    "<div class='messages'></div>" +
                    "<form><input><button>Send</button></form>" +
                    "</div>"
                );
                // Hook up send button to send a message
                roomdiv.find("form").on("submit", function() {
                    socket.send(JSON.stringify({
                        "command": "send",
                        "room": data.join,
                        "message": roomdiv.find("input").val()
                    }));
                    roomdiv.find("input").val("");
                    return false;
                });
                $("#chats").append(roomdiv);

                // Handle leaving
            } else if (data.leave) {
                console.log("Leaving room " + data.leave);
                $("#room-" + data.leave).remove();

                // Handle getting a message
            } else if (data.message || data.msg_type != 0) {
                let msgdiv = $("#room-" + data.room + " .messages");
                let ok_msg = document.createElement('div');

                switch (data.msg_type) {
                    case 0:
                        // Message
                        ok_msg.className = 'message';
                        let span_username = document.createElement('span');
                        span_username.innerText = data.username;
                        span_username.className = 'username';
                        let span_message = document.createElement('span');
                        span_message.className = 'body';
                        span_message.innerText = data.message;

                        ok_msg.innerHTML = span_username + span_message;
                        break;
                    case 1:
                        ok_msg.className = 'contextual-message text-warning';
                        ok_msg.innerText = data.message;
                        break;
                    case 2:
                        ok_msg.className = 'contextual-message text-danger';
                        ok_msg.innerText = data.message;
                        break;
                    case 3:
                        ok_msg.className = 'contextual-message text-muted';
                        ok_msg.innerText = data.message;
                        break;
                    case 4:
                        ok_msg.className = 'contextual-message text-muted';
                        ok_msg.innerText = data.username + " joined the room!";
                        break;
                    case 5:
                        ok_msg.className = 'contextual-message text-muted';
                        ok_msg.innerText = data.username + " left the room!";
                        break;
                    default:
                        console.log("Unsupported message type!");
                        return;
                }
                msgdiv.append(ok_msg);

                msgdiv.scrollTop(msgdiv.prop("scrollHeight"));
            } else {
                console.log("Cannot handle message!");
            }
        };

        // Room join/leave
        $("li.room-link").click(function() {
            roomId = $(this).attr("data-room-id");
            if (inRoom(roomId)) {
                // Leave room
                $(this).removeClass("joined");
                socket.send(JSON.stringify({
                    "command": "leave",
                    "room": roomId
                }));
            } else {
                // Join room
                $(this).addClass("joined");
                socket.send(JSON.stringify({
                    "command": "join",
                    "room": roomId
                }));
            }
        });

        // debugging
        socket.onopen = function() {
            console.log("Connected to chat socket");
        };
        socket.onclose = function() {
            console.log("Disconnected from chat socket");
        }
    });