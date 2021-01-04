# statcode

`statcode` is like `man` but for HTTP status codes. If you're a web developer, you probably spend some time looking at response codes (usually errors) and then Googling what they mean. But with `statcode`, you can simply run `$ statcode [status_code]` and get a quick explanation of your HTTP response without leaving the terminal.

![demo](assets/demo.gif)

## Installation

>Requires Python 3.0 or higher

`statcode` works on MacOS, Linux, and Windows (if you use Cygwin). You can install it with pip:

```bash
$ pip install statcode
```

Or if you're running Arch, you can install [`statcode`](https://aur.archlinux.org/packages/statcode/) from the AUR:

```bash
$ aurman -S statcode
```

## Contributing

This is a pretty small project (something I put together on a plane ride), but with enough help it could turn into a go-to manual for everything HTTP-related. If you'd like to help make this happen, feel free to fork the repo and contribute.

If you've discovered a bug or have a feature request, create an [issue](https://github.com/shobrook/statcode/issues/new) and I'll take care of it!
