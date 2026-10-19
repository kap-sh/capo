"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListTestTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_template_summary_list


class ListTestTemplatesResponse(TypedDict, closed=True):
    test_templates: (
        "capo_resiliencehubv2.types.test_template_summary_list.TestTemplateSummaryList"
    )
    """<p>The list of test template summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTestTemplatesResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.test_template_summary_list

    out["testTemplates"] = (
        capo_resiliencehubv2.types.test_template_summary_list.serialize_json(
            value["test_templates"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListTestTemplatesResponse:
    out: ListTestTemplatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("testTemplates") is not None:
        import capo_resiliencehubv2.types.test_template_summary_list

        out["test_templates"] = (
            capo_resiliencehubv2.types.test_template_summary_list.deserialize_json(
                data["testTemplates"]
            )
        )
    else:
        out["test_templates"] = []
    return out
