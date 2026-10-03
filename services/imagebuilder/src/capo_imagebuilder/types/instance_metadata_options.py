"""Generated from Smithy shape ``com.amazonaws.imagebuilder#InstanceMetadataOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.http_put_response_hop_limit
    import capo_imagebuilder.types.http_tokens


class InstanceMetadataOptions(TypedDict, closed=True):
    http_tokens: NotRequired["capo_imagebuilder.types.http_tokens.HttpTokens"]
    """<p>Indicates whether a signed token header is required for instance metadata retrieval requests. The values affect the response as follows:</p> <ul> <li> <p> <b>required</b> – When you retrieve the IAM role credentials, version 2.0 credentials are returned in all cases.</p> </li> <li> <p> <b>optional</b> – You can include a signed token header in your request to retrieve instance metadata, or you can leave it out. If you include it, version 2.0 credentials are returned for the IAM role. Otherwise, version 1.0 credentials are returned.</p> </li> </ul> <p>If you don't set a value, the EC2 launch default applies to the build and test instances. That default depends on the base AMI and any account-level instance metadata defaults. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html">Configure the instance metadata options</a> in the <i> <i>Amazon EC2 User Guide</i> </i>.</p>"""
    http_put_response_hop_limit: NotRequired[
        "capo_imagebuilder.types.http_put_response_hop_limit.HttpPutResponseHopLimit"
    ]
    """<p>Limit the number of hops that an instance metadata request can traverse to reach its destination. If you don't set a value, the EC2 launch default for the instance applies. If HTTP tokens are required, container image builds need a minimum of two hops.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceMetadataOptions) -> dict:
    out: dict = {}
    if "http_tokens" in value:
        out["httpTokens"] = value["http_tokens"]
    if "http_put_response_hop_limit" in value:
        out["httpPutResponseHopLimit"] = value["http_put_response_hop_limit"]
    return out


def deserialize_json(data: dict) -> InstanceMetadataOptions:
    out: InstanceMetadataOptions = {}  # type: ignore[typeddict-item]
    if data.get("httpTokens") is not None:
        out["http_tokens"] = data["httpTokens"]
    if data.get("httpPutResponseHopLimit") is not None:
        out["http_put_response_hop_limit"] = data["httpPutResponseHopLimit"]
    return out
