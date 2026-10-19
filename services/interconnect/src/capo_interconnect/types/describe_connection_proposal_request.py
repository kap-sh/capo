"""Generated from Smithy shape ``com.amazonaws.interconnect#DescribeConnectionProposalRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.activation_key


class DescribeConnectionProposalRequest(TypedDict, closed=True):
    activation_key: "capo_interconnect.types.activation_key.ActivationKey"
    """<p>An Activation Key that was generated on a supported partner's portal. This key captures the desired parameters from the initial creation request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeConnectionProposalRequest) -> dict:
    out: dict = {}
    out["activationKey"] = value["activation_key"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeConnectionProposalRequest:
    out: DescribeConnectionProposalRequest = {}  # type: ignore[typeddict-item]
    if data.get("activationKey") is not None:
        out["activation_key"] = data["activationKey"]
    else:
        out["activation_key"] = ""
    return out


def redact_sensitive(value: DescribeConnectionProposalRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "activation_key" in value:
        out["activation_key"] = "*** Sensitive Data Redacted ***"
    return out
