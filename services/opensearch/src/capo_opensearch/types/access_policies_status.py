"""Generated from Smithy shape ``com.amazonaws.opensearch#AccessPoliciesStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.option_status
    import capo_opensearch.types.policy_document


class AccessPoliciesStatus(TypedDict, closed=True):
    options: "capo_opensearch.types.policy_document.PolicyDocument"
    """<p>The access policy configured for the domain. Access policies can be resource-based, IP-based, or IAM-based. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-access-policies">Configuring access policies</a>.</p>"""
    status: "capo_opensearch.types.option_status.OptionStatus"
    """<p>The status of the access policy for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessPoliciesStatus) -> dict:
    out: dict = {}
    out["Options"] = value["options"]
    import capo_opensearch.types.option_status

    out["Status"] = capo_opensearch.types.option_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> AccessPoliciesStatus:
    out: AccessPoliciesStatus = {}  # type: ignore[typeddict-item]
    if data.get("Options") is not None:
        out["options"] = data["Options"]
    else:
        raise DeserializationError("AccessPoliciesStatus.options required")
    if data.get("Status") is not None:
        import capo_opensearch.types.option_status

        out["status"] = capo_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("AccessPoliciesStatus.status required")
    return out
