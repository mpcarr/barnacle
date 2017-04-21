

class BrowseSources:

  self.sources = []

  def __init__(self, socket):
      socket.on('pushBrowseSources', self.on_browseSources)
      socket.emit('getBrowseSources')
      socket.wait(seconds=1)

  def on_browseSources(self, *args):
    data = json.dumps(args[0])
    data = json.loads(data)
    self.sources = data


  def render(self):
    print("")