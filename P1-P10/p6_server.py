'''
https://www.bilibili.com/video/BV1Gr42e1EDq?spm_id_from=333.788.player.switch&vd_source=bde8a6c551fd6e4478561ee775490a98&p=6
'''
import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 8090))
sock.listen(5)
while True:
    conn, addr = sock.accept()  # 阻塞等待,等待客户端连接
    data = conn.recv(1024)  # 这个是浏览器通过管道 conn 发送的数据
    print("客户端发送的请求信息:\n", data)

    # 对于服务器来讲, 产生的响应需要一定的格式,才能在浏览器中显示页面.
    # conn.send(b"HTTP/1.1 200 OK\r\nserver_name:simon.xu\r\ncontent-type:text/html\r\n\r\n<h1>hello world</h1>")
    conn.send(b'HTTP/1.1 200 OK\r\nserver_name:simon.xu\r\ncontent-type:application/json\r\n\r\n{"useid":101}')
    conn.close()
    print("**************************")
