#!/usr/bin/env python3

import config

def main():
    app = config.connex_app
    app.add_api('openapi.yaml',
                arguments={'title': 'Book CRUD API'},
                pythonic_params=True)

    app.run(port=8080)


if __name__ == '__main__':
    main()
