"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AccessPoliciesStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.option_status
    import capo_elasticsearch_service.types.policy_document


class AccessPoliciesStatus(TypedDict, closed=True):
    options: "capo_elasticsearch_service.types.policy_document.PolicyDocument"
    """<p>The access policy configured for the Elasticsearch domain. Access policies may be resource-based, IP-based, or IAM-based. See <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-access-policies" target="_blank"> Configuring Access Policies</a>for more information.</p>"""
    status: "capo_elasticsearch_service.types.option_status.OptionStatus"
    """<p>The status of the access policy for the Elasticsearch domain. See <code>OptionStatus</code> for the status information that's included. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessPoliciesStatus) -> dict:
    out: dict = {}
    out["Options"] = value["options"]
    import capo_elasticsearch_service.types.option_status

    out["Status"] = capo_elasticsearch_service.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> AccessPoliciesStatus:
    out: AccessPoliciesStatus = {}  # type: ignore[typeddict-item]
    if data.get("Options") is not None:
        out["options"] = data["Options"]
    else:
        raise DeserializationError("AccessPoliciesStatus.options required")
    if data.get("Status") is not None:
        import capo_elasticsearch_service.types.option_status

        out["status"] = capo_elasticsearch_service.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("AccessPoliciesStatus.status required")
    return out
