import socket
import threading
import pickle

# 配置服务器
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen()

clients = []
positions = {}

def handle_client(client_socket, addr):
    global positions
    print(f"[连接] {addr} 已连接")
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            positions[addr] = pickle.loads(data)
            print(f"[接收] 来自 {addr} 的数据: {positions[addr]}")
            broadcast_positions()
        except Exception as e:
            print(f"[错误] {addr} 连接出错: {e}")
            clients.remove(client_socket)
            del positions[addr]
            client_socket.close()
            break

def broadcast_positions():
    for client in clients:
        try:
            client.send(pickle.dumps(positions))
            print(f"[发送] 广播数据: {positions}")
        except Exception as e:
            print(f"[错误] 广播出错: {e}")
            clients.remove(client)
            client.close()

def main():
    print("[启动] 服务器启动...")
    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        positions[addr] = (0, 0)
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

if __name__ == "__main__":
    main()
