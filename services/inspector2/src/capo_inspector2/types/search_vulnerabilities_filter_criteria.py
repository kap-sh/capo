"""Generated from Smithy shape ``com.amazonaws.inspector2#SearchVulnerabilitiesFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.vuln_id_list


class SearchVulnerabilitiesFilterCriteria(TypedDict, closed=True):
    vulnerability_ids: "capo_inspector2.types.vuln_id_list.VulnIdList"
    """<p>The IDs for specific vulnerabilities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchVulnerabilitiesFilterCriteria) -> dict:
    out: dict = {}
    import capo_inspector2.types.vuln_id_list

    out["vulnerabilityIds"] = capo_inspector2.types.vuln_id_list.serialize_json(
        value["vulnerability_ids"]
    )
    return out


def deserialize_json(data: dict) -> SearchVulnerabilitiesFilterCriteria:
    out: SearchVulnerabilitiesFilterCriteria = {}  # type: ignore[typeddict-item]
    if data.get("vulnerabilityIds") is not None:
        import capo_inspector2.types.vuln_id_list

        out["vulnerability_ids"] = capo_inspector2.types.vuln_id_list.deserialize_json(
            data["vulnerabilityIds"]
        )
    else:
        out["vulnerability_ids"] = []
    return out
