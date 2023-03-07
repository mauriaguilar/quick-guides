# Launch Android Studio for Flutter apps

## Build docker image
    ```bash
    make build
    ```
## Launch docker image
    ```bash
    make # or make run
    ```

## Configurations
* Follow install proccess.
* Install Dart Plugin:
  ![dart](./docs/a.png)
* Install Flutter Plugin:
  ![flutter1](./docs/b.png)
  ![flutter2](./docs/c.png)
* Restart the IDE:
    ```bash
    make # or make run or make res
    ```
* Go to "More Actions" and click on "SDK Manager":
  ![sdkmanager](./docs/d.png)
* Go To SDK Tools and install:
  * Android SDK Build-Tools
  * Android SDK Command-Line Tools
  ![tools](./docs/e.png)
* Create a new Flutter Project:
  ![flutterproject](./docs/f.png)
* Select Flutter and set the Flutter SDK Path:
  ![fluttersdk](./docs/g.png)
* Next and Complete the info.
  ![flutterprojectinfo](./docs/i.png)
