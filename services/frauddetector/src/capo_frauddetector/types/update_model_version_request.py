"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateModelVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.external_events_detail
    import capo_frauddetector.types.ingested_events_detail
    import capo_frauddetector.types.model_identifier
    import capo_frauddetector.types.model_type_enum
    import capo_frauddetector.types.tag_list
    import capo_frauddetector.types.whole_number_version_string


class UpdateModelVersionRequest(TypedDict, closed=True):
    model_id: "capo_frauddetector.types.model_identifier.modelIdentifier"
    """<p>The model ID.</p>"""
    model_type: "capo_frauddetector.types.model_type_enum.ModelTypeEnum"
    """<p>The model type.</p>"""
    major_version_number: (
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    )
    """<p>The major version number.</p>"""
    external_events_detail: NotRequired[
        "capo_frauddetector.types.external_events_detail.ExternalEventsDetail"
    ]
    """<p>The details of the external events data used for training the model version. Required if <code>trainingDataSource</code> is <code>EXTERNAL_EVENTS</code>.</p>"""
    ingested_events_detail: NotRequired[
        "capo_frauddetector.types.ingested_events_detail.IngestedEventsDetail"
    ]
    """<p>The details of the ingested event used for training the model version. Required if your <code>trainingDataSource</code> is <code>INGESTED_EVENTS</code>.</p>"""
    tags: NotRequired["capo_frauddetector.types.tag_list.tagList"]
    """<p>A collection of key and value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateModelVersionRequest) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    import capo_frauddetector.types.model_type_enum

    out["modelType"] = capo_frauddetector.types.model_type_enum.serialize_aws_json_1_1(
        value["model_type"]
    )
    out["majorVersionNumber"] = value["major_version_number"]
    if "external_events_detail" in value:
        import capo_frauddetector.types.external_events_detail

        out["externalEventsDetail"] = (
            capo_frauddetector.types.external_events_detail.serialize_aws_json_1_1(
                value["external_events_detail"]
            )
        )
    if "ingested_events_detail" in value:
        import capo_frauddetector.types.ingested_events_detail

        out["ingestedEventsDetail"] = (
            capo_frauddetector.types.ingested_events_detail.serialize_aws_json_1_1(
                value["ingested_events_detail"]
            )
        )
    if "tags" in value:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateModelVersionRequest:
    out: UpdateModelVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    if data.get("modelType") is not None:
        import capo_frauddetector.types.model_type_enum

        out["model_type"] = (
            capo_frauddetector.types.model_type_enum.deserialize_aws_json_1_1(
                data["modelType"]
            )
        )
    else:
        import typing

        out["model_type"] = typing.cast(
            "capo_frauddetector.types.model_type_enum.ModelTypeEnum", ""
        )
    if data.get("majorVersionNumber") is not None:
        out["major_version_number"] = data["majorVersionNumber"]
    else:
        out["major_version_number"] = ""
    if data.get("externalEventsDetail") is not None:
        import capo_frauddetector.types.external_events_detail

        out["external_events_detail"] = (
            capo_frauddetector.types.external_events_detail.deserialize_aws_json_1_1(
                data["externalEventsDetail"]
            )
        )
    if data.get("ingestedEventsDetail") is not None:
        import capo_frauddetector.types.ingested_events_detail

        out["ingested_events_detail"] = (
            capo_frauddetector.types.ingested_events_detail.deserialize_aws_json_1_1(
                data["ingestedEventsDetail"]
            )
        )
    if data.get("tags") is not None:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
