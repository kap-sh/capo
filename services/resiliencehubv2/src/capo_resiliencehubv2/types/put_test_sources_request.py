"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PutTestSourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.test_id
    import capo_resiliencehubv2.types.test_source_input_list


class PutTestSourcesRequest(TypedDict, closed=True):
    test_id: "capo_resiliencehubv2.types.test_id.TestId"
    """<p>The identifier of the test to add sources to.</p>"""
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    """<p>The ARN of the service the test belongs to.</p>"""
    test_sources: (
        "capo_resiliencehubv2.types.test_source_input_list.TestSourceInputList"
    )
    """<p>The monitoring sources to add or update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTestSourcesRequest) -> dict:
    out: dict = {}
    out["testId"] = value["test_id"]
    out["serviceArn"] = value["service_arn"]
    import capo_resiliencehubv2.types.test_source_input_list

    out["testSources"] = (
        capo_resiliencehubv2.types.test_source_input_list.serialize_json(
            value["test_sources"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutTestSourcesRequest:
    out: PutTestSourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("testId") is not None:
        out["test_id"] = data["testId"]
    else:
        out["test_id"] = ""
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("testSources") is not None:
        import capo_resiliencehubv2.types.test_source_input_list

        out["test_sources"] = (
            capo_resiliencehubv2.types.test_source_input_list.deserialize_json(
                data["testSources"]
            )
        )
    else:
        out["test_sources"] = []
    return out
