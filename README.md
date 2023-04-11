# Aparat Streamer

A Python program for streaming video to [aparat.com](https://www.aparat.com/) using the [vidgear](https://github.com/abhiTronix/vidgear) library. This program allows you to stream video from a specified location to Aparat using a provided stream key. It also includes a CLI interface for easy configuration and usage.

## Features

- Stream video to Aparat using a stream key
- Supports various video sources (e.g., webcam, video file)
- Uses FFmpeg optimizing parameters for video encoding
- CLI interface for easy configuration and usage

## Requirements

- Python 3.7+
- vidgear library

## Installation

1. Clone the repository to your local machine:

```bash
$ git clone https://github.com/ghalbeyou/aparat-streamer
```

2. Install the required dependencies:

```bash
$ pip install -r requirements.txt
```

## Usage

1. Configure the stream by editing the `config.json` file or by providing command-line arguments using the CLI interface. The available configuration options are:

- `stream_video_location`: The location of the video source to be streamed (e.g., webcam index, video file path)
- `stream_key`: The stream key provided by Aparat

2. Start the streaming program by running `main.py` or `CLI.Streamer.py`:


```bash
$ python main.py
```

or

```bash
$ python cli.py -k <stream_key> -l <stream_video_location>
```

3. The program will start streaming the video to Aparat using the provided stream key.

## Contributing

If you would like to contribute to this project, you can do so by:

- Forking the repository
- Creating a new branch
- Making your changes
- Submitting a pull request

Please make sure to follow the [Contributing Guidelines](CONTRIBUTING.md) when contributing to this project.

## License

This project is licensed under the [GNU GENERAL PUBLIC LICENSE](LICENSE).

## Acknowledgements

- [vidgear](https://github.com/abhiTronix/vidgear) library for video streaming
- [colorama](https://pypi.org/project/colorama/) library for colorful CLI output

