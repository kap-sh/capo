"""Generated from Smithy shape ``com.amazonaws.interconnect#DescribeConnectionProposalResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.connection_bandwidth
    import capo_interconnect.types.environment_id
    import capo_interconnect.types.location
    import capo_interconnect.types.provider


class DescribeConnectionProposalResponse(TypedDict, closed=True):
    bandwidth: "capo_interconnect.types.connection_bandwidth.ConnectionBandwidth"
    """<p>The bandwidth of the proposed <a>Connection</a>. </p>"""
    environment_id: "capo_interconnect.types.environment_id.EnvironmentId"
    """<p>The identifier of the <a>Environment</a> upon which the <a>Connection</a> would be placed if this proposal were accepted.</p>"""
    provider: "capo_interconnect.types.provider.Provider"
    """<p>The partner provider of the specific <a>Environment</a> of the proposal.</p>"""
    location: "capo_interconnect.types.location.Location"
    """<p>The partner specific location distinguisher of the specific <a>Environment</a> of the proposal.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeConnectionProposalResponse) -> dict:
    out: dict = {}
    out["bandwidth"] = value["bandwidth"]
    out["environmentId"] = value["environment_id"]
    import capo_interconnect.types.provider

    out["provider"] = capo_interconnect.types.provider.serialize_aws_json_1_0(
        value["provider"]
    )
    out["location"] = value["location"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeConnectionProposalResponse:
    out: DescribeConnectionProposalResponse = {}  # type: ignore[typeddict-item]
    if data.get("bandwidth") is not None:
        out["bandwidth"] = data["bandwidth"]
    else:
        out["bandwidth"] = ""
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("provider") is not None:
        import capo_interconnect.types.provider

        out["provider"] = capo_interconnect.types.provider.deserialize_aws_json_1_0(
            data["provider"]
        )
    else:
        import capo_interconnect.types._unknown

        out["provider"] = capo_interconnect.types._unknown.UnknownUnionMember("")
    if data.get("location") is not None:
        out["location"] = data["location"]
    else:
        out["location"] = ""
    return out
