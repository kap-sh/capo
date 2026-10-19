"""Generated from Smithy shape ``com.amazonaws.interconnect#AcceptConnectionProposalRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.activation_key
    import capo_interconnect.types.attach_point
    import capo_interconnect.types.connection_description
    import capo_interconnect.types.tag_map


class AcceptConnectionProposalRequest(TypedDict, closed=True):
    attach_point: "capo_interconnect.types.attach_point.AttachPoint"
    """<p>The Attach Point to which the connection should be associated.</p>"""
    activation_key: "capo_interconnect.types.activation_key.ActivationKey"
    """<p>An Activation Key that was generated on a supported partner's portal. This key captures the desired parameters from the initial creation request.</p> <p>The details of this request can be described using with <a>DescribeConnectionProposal</a>. </p>"""
    description: NotRequired[
        "capo_interconnect.types.connection_description.ConnectionDescription"
    ]
    """<p>A description to distinguish this <a>Connection</a>.</p>"""
    tags: NotRequired["capo_interconnect.types.tag_map.TagMap"]
    """<p>The tags to associate with the resulting <a>Connection</a>.</p>"""
    client_token: NotRequired["str"]
    """<p>Idempotency token used for the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptConnectionProposalRequest) -> dict:
    out: dict = {}
    import capo_interconnect.types.attach_point

    out["attachPoint"] = capo_interconnect.types.attach_point.serialize_aws_json_1_0(
        value["attach_point"]
    )
    out["activationKey"] = value["activation_key"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_interconnect.types.tag_map

        out["tags"] = capo_interconnect.types.tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptConnectionProposalRequest:
    out: AcceptConnectionProposalRequest = {}  # type: ignore[typeddict-item]
    if data.get("attachPoint") is not None:
        import capo_interconnect.types.attach_point

        out["attach_point"] = (
            capo_interconnect.types.attach_point.deserialize_aws_json_1_0(
                data["attachPoint"]
            )
        )
    else:
        import capo_interconnect.types._unknown

        out["attach_point"] = capo_interconnect.types._unknown.UnknownUnionMember("")
    if data.get("activationKey") is not None:
        out["activation_key"] = data["activationKey"]
    else:
        out["activation_key"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_interconnect.types.tag_map

        out["tags"] = capo_interconnect.types.tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: AcceptConnectionProposalRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "activation_key" in value:
        out["activation_key"] = "*** Sensitive Data Redacted ***"
    return out
