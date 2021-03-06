const {
  app,
  BrowserWindow,
} = require('electron');

/*
const python = require('python.node');
const os = pythonimport('os');
const path = require('path');
const { assert, timeStamp } = require('console');

assert(os.path.basename(os.getcwd()) == path.basename(process.cwd()));

def test():
try:
print('running py inside electron')
except Exception as e:
raise e
return 'done'

PYMODULE.test.async = true;
PYMODULE.test(function (result, error) {
  if (!error) {
    console.log(result);
  }
});
*/

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    backgroundColor: '#EEE',
    color: '#000',
    webPreferences: {
      nodeIntegration: true
    },
  });

  win.loadFile('index.html');
}

function getPythonCode() {
  var spawn = require('child_process').spawn;

  var process = spawn('python', ["./server.py"], 1234);

  process.stdout.on('data', function (data) {
    console.log(data.toString());
  })
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
    getPythonCode();
  }
});