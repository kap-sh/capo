"""Generated from Smithy shape ``com.amazonaws.directoryservice#DisableClientAuthenticationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.client_authentication_type
    import capo_directory_service.types.directory_id


class DisableClientAuthenticationRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory </p>"""
    type: "capo_directory_service.types.client_authentication_type.ClientAuthenticationType"
    """<p>The type of client authentication to disable. Currently the only parameter <code>"SmartCard"</code> is supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableClientAuthenticationRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import capo_directory_service.types.client_authentication_type

    out["Type"] = (
        capo_directory_service.types.client_authentication_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableClientAuthenticationRequest:
    out: DisableClientAuthenticationRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("Type") is not None:
        import capo_directory_service.types.client_authentication_type

        out["type"] = (
            capo_directory_service.types.client_authentication_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_directory_service.types.client_authentication_type.ClientAuthenticationType",
            "",
        )
    return out
