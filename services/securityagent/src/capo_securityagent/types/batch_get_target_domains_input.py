"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetTargetDomainsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.target_domain_id_list


class BatchGetTargetDomainsInput(TypedDict, closed=True):
    target_domain_ids: (
        "capo_securityagent.types.target_domain_id_list.TargetDomainIdList"
    )
    """<p>The list of target domain identifiers to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTargetDomainsInput) -> dict:
    out: dict = {}
    import capo_securityagent.types.target_domain_id_list

    out["targetDomainIds"] = (
        capo_securityagent.types.target_domain_id_list.serialize_json(
            value["target_domain_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetTargetDomainsInput:
    out: BatchGetTargetDomainsInput = {}  # type: ignore[typeddict-item]
    if data.get("targetDomainIds") is not None:
        import capo_securityagent.types.target_domain_id_list

        out["target_domain_ids"] = (
            capo_securityagent.types.target_domain_id_list.deserialize_json(
                data["targetDomainIds"]
            )
        )
    else:
        out["target_domain_ids"] = []
    return out
