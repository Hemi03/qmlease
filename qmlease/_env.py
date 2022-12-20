import os
from importlib.util import find_spec


def find_qt_api() -> str:
    """
    this should be called before importing qtpy.
    refer: `lib:qtpy/__init__.py`
    """
    api = os.getenv('QT_API', '')
    
    if not api:
        for pkg, api in {
            'PySide6'     : 'pyside6',
            'PyQt6'       : 'pyqt6',
            'PySide2'     : 'pyside2',
            'PyQt5'       : 'pyqt5',
            'pyside6_lite': 'pyside6'
        }.items():
            if find_spec(pkg):
                if pkg == 'pyside6_lite':
                    # see `sidework/pyside_package_tailor/dist/pyside6_lite`.
                    # activate special pyside6 location.
                    import pyside6_lite  # noqa
                print(':v2', f'auto detected qt api: {api}')
                os.environ['QT_API'] = api
                break
        else:
            raise ModuleNotFoundError('no qt bindings found!')
    
    if api == 'pyside2':
        # try to repair pyside2 highdpi issue
        #   https://www.hwang.top/post/pyside2pyqt-zai-windows-zhong-tian-jia
        #   -dui-gao-fen-ping-de-zhi-chi/
        # warning: this must be called before QCoreApplication is created.
        from PySide2 import QtCore  # noqa
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    
    return api


QT_API = find_qt_api()
