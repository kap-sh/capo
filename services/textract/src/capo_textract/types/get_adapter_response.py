"""Generated from Smithy shape ``com.amazonaws.textract#GetAdapterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.adapter_description
    import capo_textract.types.adapter_id
    import capo_textract.types.adapter_name
    import capo_textract.types.auto_update
    import capo_textract.types.date_time
    import capo_textract.types.feature_types
    import capo_textract.types.tag_map


class GetAdapterResponse(TypedDict, closed=True):
    adapter_id: NotRequired["capo_textract.types.adapter_id.AdapterId"]
    """<p>A string identifying the adapter that information has been retrieved for.</p>"""
    adapter_name: NotRequired["capo_textract.types.adapter_name.AdapterName"]
    """<p>The name of the requested adapter.</p>"""
    creation_time: NotRequired["capo_textract.types.date_time.DateTime"]
    """<p>The date and time the requested adapter was created at.</p>"""
    description: NotRequired[
        "capo_textract.types.adapter_description.AdapterDescription"
    ]
    """<p>The description for the requested adapter.</p>"""
    feature_types: NotRequired["capo_textract.types.feature_types.FeatureTypes"]
    """<p>List of the targeted feature types for the requested adapter.</p>"""
    auto_update: NotRequired["capo_textract.types.auto_update.AutoUpdate"]
    """<p>Binary value indicating if the adapter is being automatically updated or not.</p>"""
    tags: NotRequired["capo_textract.types.tag_map.TagMap"]
    """<p>A set of tags (key-value pairs) associated with the adapter that has been retrieved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAdapterResponse) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    if "adapter_name" in value:
        out["AdapterName"] = value["adapter_name"]
    if "creation_time" in value:
        import capo_textract.types.date_time

        out["CreationTime"] = capo_textract.types.date_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "feature_types" in value:
        import capo_textract.types.feature_types

        out["FeatureTypes"] = capo_textract.types.feature_types.serialize_aws_json_1_1(
            value["feature_types"]
        )
    if "auto_update" in value:
        import capo_textract.types.auto_update

        out["AutoUpdate"] = capo_textract.types.auto_update.serialize_aws_json_1_1(
            value["auto_update"]
        )
    if "tags" in value:
        import capo_textract.types.tag_map

        out["Tags"] = capo_textract.types.tag_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAdapterResponse:
    out: GetAdapterResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdapterId") is not None:
        out["adapter_id"] = data["AdapterId"]
    if data.get("AdapterName") is not None:
        out["adapter_name"] = data["AdapterName"]
    if data.get("CreationTime") is not None:
        import capo_textract.types.date_time

        out["creation_time"] = capo_textract.types.date_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FeatureTypes") is not None:
        import capo_textract.types.feature_types

        out["feature_types"] = (
            capo_textract.types.feature_types.deserialize_aws_json_1_1(
                data["FeatureTypes"]
            )
        )
    if data.get("AutoUpdate") is not None:
        import capo_textract.types.auto_update

        out["auto_update"] = capo_textract.types.auto_update.deserialize_aws_json_1_1(
            data["AutoUpdate"]
        )
    if data.get("Tags") is not None:
        import capo_textract.types.tag_map

        out["tags"] = capo_textract.types.tag_map.deserialize_aws_json_1_1(data["Tags"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAdapterResponse) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    if "adapter_name" in value:
        out["AdapterName"] = value["adapter_name"]
    if "creation_time" in value:
        import capo_textract.types.date_time

        out["CreationTime"] = capo_textract.types.date_time.serialize_cbor(
            value["creation_time"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "feature_types" in value:
        import capo_textract.types.feature_types

        out["FeatureTypes"] = capo_textract.types.feature_types.serialize_cbor(
            value["feature_types"]
        )
    if "auto_update" in value:
        import capo_textract.types.auto_update

        out["AutoUpdate"] = capo_textract.types.auto_update.serialize_cbor(
            value["auto_update"]
        )
    if "tags" in value:
        import capo_textract.types.tag_map

        out["Tags"] = capo_textract.types.tag_map.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> GetAdapterResponse:
    out: GetAdapterResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdapterId") is not None:
        out["adapter_id"] = data["AdapterId"]
    if data.get("AdapterName") is not None:
        out["adapter_name"] = data["AdapterName"]
    if data.get("CreationTime") is not None:
        import capo_textract.types.date_time

        out["creation_time"] = capo_textract.types.date_time.deserialize_cbor(
            data["CreationTime"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FeatureTypes") is not None:
        import capo_textract.types.feature_types

        out["feature_types"] = capo_textract.types.feature_types.deserialize_cbor(
            data["FeatureTypes"]
        )
    if data.get("AutoUpdate") is not None:
        import capo_textract.types.auto_update

        out["auto_update"] = capo_textract.types.auto_update.deserialize_cbor(
            data["AutoUpdate"]
        )
    if data.get("Tags") is not None:
        import capo_textract.types.tag_map

        out["tags"] = capo_textract.types.tag_map.deserialize_cbor(data["Tags"])
    return out
