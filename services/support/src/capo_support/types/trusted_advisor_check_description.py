"""Generated from Smithy shape ``com.amazonaws.support#TrustedAdvisorCheckDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support.types.string
    import capo_support.types.string_list


class TrustedAdvisorCheckDescription(TypedDict, closed=True):
    id: "capo_support.types.string.String"
    """<p>The unique identifier for the Trusted Advisor check.</p>"""
    name: "capo_support.types.string.String"
    """<p>The display name for the Trusted Advisor check.</p>"""
    description: "capo_support.types.string.String"
    """<p>The description of the Trusted Advisor check, which includes the alert criteria and recommended operations (contains HTML markup).</p>"""
    category: "capo_support.types.string.String"
    """<p>The category of the Trusted Advisor check.</p>"""
    metadata: "capo_support.types.string_list.StringList"
    """<p>The column headings for the data returned by the Trusted Advisor check. The order of the headings corresponds to the order of the data in the <b>Metadata</b> element of the <a>TrustedAdvisorResourceDetail</a> for the check. <b>Metadata</b> contains all the data that is shown in the Excel download, even in those cases where the UI shows just summary data. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedAdvisorCheckDescription) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    out["category"] = value["category"]
    import capo_support.types.string_list

    out["metadata"] = capo_support.types.string_list.serialize_aws_json_1_1(
        value["metadata"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrustedAdvisorCheckDescription:
    out: TrustedAdvisorCheckDescription = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("category") is not None:
        out["category"] = data["category"]
    else:
        out["category"] = ""
    if data.get("metadata") is not None:
        import capo_support.types.string_list

        out["metadata"] = capo_support.types.string_list.deserialize_aws_json_1_1(
            data["metadata"]
        )
    else:
        out["metadata"] = []
    return out
