import socketio from 'socket.io-client';

const socket = socketio('https://example.com');

export default function useSocket() {
    return socket;
}
