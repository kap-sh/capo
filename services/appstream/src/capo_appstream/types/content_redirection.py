"""Generated from Smithy shape ``com.amazonaws.appstream#ContentRedirection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.url_redirection_config


class ContentRedirection(TypedDict, closed=True):
    host_to_client: NotRequired[
        "capo_appstream.types.url_redirection_config.UrlRedirectionConfig"
    ]
    """<p>Configuration for redirecting URLs from the remote desktop to the local client browser.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentRedirection) -> dict:
    out: dict = {}
    if "host_to_client" in value:
        import capo_appstream.types.url_redirection_config

        out["HostToClient"] = (
            capo_appstream.types.url_redirection_config.serialize_aws_json_1_1(
                value["host_to_client"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContentRedirection:
    out: ContentRedirection = {}  # type: ignore[typeddict-item]
    if data.get("HostToClient") is not None:
        import capo_appstream.types.url_redirection_config

        out["host_to_client"] = (
            capo_appstream.types.url_redirection_config.deserialize_aws_json_1_1(
                data["HostToClient"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContentRedirection) -> dict:
    out: dict = {}
    if "host_to_client" in value:
        import capo_appstream.types.url_redirection_config

        out["HostToClient"] = (
            capo_appstream.types.url_redirection_config.serialize_cbor(
                value["host_to_client"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ContentRedirection:
    out: ContentRedirection = {}  # type: ignore[typeddict-item]
    if data.get("HostToClient") is not None:
        import capo_appstream.types.url_redirection_config

        out["host_to_client"] = (
            capo_appstream.types.url_redirection_config.deserialize_cbor(
                data["HostToClient"]
            )
        )
    return out
