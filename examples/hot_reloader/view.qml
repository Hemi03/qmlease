import QtQuick 2.15
import QtQuick.Window 2.15

Window {
    visible: true
    width: 400
    height: 300
    color: 'white'  // change to 'yellow', 'red', etc. then reload.

    Text {
        anchors.centerIn: parent
        text: 'Hello world!'
    }
}
