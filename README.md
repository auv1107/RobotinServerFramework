
  一个简要的指令型服务器框架
  
  
##用法
  
  1. import Server类
  ```
  from robotin.server import Server
  ```
  
  2. 配置自己的服务器参数
  ```
  # Server(SocketType, Port)
  server = Server('udp', 8007)
  ```
  如果需要建立tcp连接， 则把第一个参数改为'tcp'
  
  3. 添加服务器可处理的指令
  ```
  f = server.factory
  @f.handler('mousedown')
  def mouse_down(data):
        """处理鼠标点击事件"""
        pass
        
  @f.handler('key_taped')
  def key_taped(data):
        """处理键盘按键事件"""
        pass
        
  # 自定义更多指令
  # @f.handler(EventType)
  # def event_handler(instruction_made_with_client):
  #     handle_this_event_here()
  ```
  
  4. 开始监听
  ```
  server.listen()
  ```
