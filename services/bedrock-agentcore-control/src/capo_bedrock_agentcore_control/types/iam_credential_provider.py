"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#IamCredentialProvider``."""

from typing_extensions import NotRequired, TypedDict


class IamCredentialProvider(TypedDict, closed=True):
    service: "str"
    """<p>The target Amazon Web Services service name used for SigV4 signing. This value identifies the service that the gateway authenticates with when making requests to the target endpoint.</p>"""
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region used for SigV4 signing. If not specified, defaults to the gateway's Region.</p>"""


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
