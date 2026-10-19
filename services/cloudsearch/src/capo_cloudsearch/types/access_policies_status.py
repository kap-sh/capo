"""Generated from Smithy shape ``com.amazonaws.cloudsearch#AccessPoliciesStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.option_status
    import capo_cloudsearch.types.policy_document


class AccessPoliciesStatus(TypedDict, closed=True):
    options: "capo_cloudsearch.types.policy_document.PolicyDocument"
    status: "capo_cloudsearch.types.option_status.OptionStatus"


# --- awsQuery ser/de ---
def serialize_query(
    value: AccessPoliciesStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Options", str(value["options"])))
    import capo_cloudsearch.types.option_status

    capo_cloudsearch.types.option_status.serialize_query(
        value["status"], pairs, f"{key_prefix}Status"
    )


def deserialize_query(el: Element) -> AccessPoliciesStatus:
    out: AccessPoliciesStatus = {}  # type: ignore[typeddict-item]
    child_options = el.find("Options")
    if child_options is not None:
        out["options"] = str(child_options.text or "")
    else:
        out["options"] = ""
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudsearch.types.option_status

        out["status"] = capo_cloudsearch.types.option_status.deserialize_query(
            child_status
        )
    else:
        raise DeserializationError("AccessPoliciesStatus.status required")
    return out
