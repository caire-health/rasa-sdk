import argparse

from rasa_sdk.constants import DEFAULT_SERVER_PORT, DEFAULT_ENDPOINTS_PATH


def action_arg(action):
    if "/" in action:
        raise argparse.ArgumentTypeError(
            "Invalid actions format. Actions file should be a python module "
            "and passed with module notation (e.g. directory.actions)."
        )
    else:
        return action


def add_endpoint_arguments(parser):
    parser.add_argument(
        "-p",
        "--port",
        default=DEFAULT_SERVER_PORT,
        type=int,
        help="port to run the server at",
    )
    parser.add_argument(
        "--cors",
        nargs="*",
        type=str,
        help="enable CORS for the passed origin. Use * to whitelist all origins",
    )
    parser.add_argument(
        "--actions",
        type=action_arg,
        default=None,
        help="name of action package to be loaded",
    )
    parser.add_argument(
        "--ssl-keyfile",
        default=None,
        help="Set the SSL certificate to create a TLS secured server.",
    )
    parser.add_argument(
        "--ssl-certificate",
        default=None,
        help="Set the SSL certificate to create a TLS secured server.",
    )
    parser.add_argument(
        "--ssl-password",
        default=None,
        help="If your ssl-keyfile is protected by a password, you can specify it "
        "using this paramer.",
    )
    parser.add_argument(
        "--auto-reload",
        help="Enable auto-reloading of modules containing Action subclasses.",
        action="store_true",
    )
    parser.add_argument(
        "--endpoints",
        default=DEFAULT_ENDPOINTS_PATH,
        help="Configuration file for the assistant as a yml file.",
    )
    parser.add_argument(
        "--grpc",
        help="Starts grpc server instead of http",
        action="store_true"
    )
