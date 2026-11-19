"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#IamCredentialProvider``."""

from typing_extensions import NotRequired, TypedDict


class IamCredentialProvider(TypedDict, closed=True):
    service: "str"
    """<p>The name of the Amazon Web Services service used for SigV4 signing. This value identifies the service to authenticate with when sending requests to the target endpoint.</p>"""
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region used for SigV4 signing. If not specified, defaults to the Region of the resource that makes the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamCredentialProvider) -> dict:
    out: dict = {}
    out["service"] = value["service"]
    if "region" in value:
        out["region"] = value["region"]
    return out


def deserialize_json(data: dict) -> IamCredentialProvider:
    out: IamCredentialProvider = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        out["service"] = data["service"]
    else:
        out["service"] = ""
    if data.get("region") is not None:
        out["region"] = data["region"]
    return out
