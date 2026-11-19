"""Generated from Smithy shape ``com.amazonaws.textract#AdapterVersionOverview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.adapter_id
    import capo_textract.types.adapter_version
    import capo_textract.types.adapter_version_status
    import capo_textract.types.adapter_version_status_message
    import capo_textract.types.date_time
    import capo_textract.types.feature_types


class AdapterVersionOverview(TypedDict, closed=True):
    adapter_id: NotRequired["capo_textract.types.adapter_id.AdapterId"]
    """<p>A unique identifier for the adapter associated with a given adapter version.</p>"""
    adapter_version: NotRequired["capo_textract.types.adapter_version.AdapterVersion"]
    """<p>An identified for a given adapter version.</p>"""
    creation_time: NotRequired["capo_textract.types.date_time.DateTime"]
    """<p>The date and time that a given adapter version was created.</p>"""
    feature_types: NotRequired["capo_textract.types.feature_types.FeatureTypes"]
    """<p>The feature types that the adapter version is operating on.</p>"""
    status: NotRequired[
        "capo_textract.types.adapter_version_status.AdapterVersionStatus"
    ]
    """<p>Contains information on the status of a given adapter version.</p>"""
    status_message: NotRequired[
        "capo_textract.types.adapter_version_status_message.AdapterVersionStatusMessage"
    ]
    """<p>A message explaining the status of a given adapter vesion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdapterVersionOverview) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    if "adapter_version" in value:
        out["AdapterVersion"] = value["adapter_version"]
    if "creation_time" in value:
        import capo_textract.types.date_time

        out["CreationTime"] = capo_textract.types.date_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "feature_types" in value:
        import capo_textract.types.feature_types

        out["FeatureTypes"] = capo_textract.types.feature_types.serialize_aws_json_1_1(
            value["feature_types"]
        )
    if "status" in value:
        import capo_textract.types.adapter_version_status

        out["Status"] = (
            capo_textract.types.adapter_version_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AdapterVersionOverview:
    out: AdapterVersionOverview = {}  # type: ignore[typeddict-item]
    if data.get("AdapterId") is not None:
        out["adapter_id"] = data["AdapterId"]
    if data.get("AdapterVersion") is not None:
        out["adapter_version"] = data["AdapterVersion"]
    if data.get("CreationTime") is not None:
        import capo_textract.types.date_time

        out["creation_time"] = capo_textract.types.date_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("FeatureTypes") is not None:
        import capo_textract.types.feature_types

        out["feature_types"] = (
            capo_textract.types.feature_types.deserialize_aws_json_1_1(
                data["FeatureTypes"]
            )
        )
    if data.get("Status") is not None:
        import capo_textract.types.adapter_version_status

        out["status"] = (
            capo_textract.types.adapter_version_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AdapterVersionOverview) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    if "adapter_version" in value:
        out["AdapterVersion"] = value["adapter_version"]
    if "creation_time" in value:
        import capo_textract.types.date_time

        out["CreationTime"] = capo_textract.types.date_time.serialize_cbor(
            value["creation_time"]
        )
    if "feature_types" in value:
        import capo_textract.types.feature_types

        out["FeatureTypes"] = capo_textract.types.feature_types.serialize_cbor(
            value["feature_types"]
        )
    if "status" in value:
        import capo_textract.types.adapter_version_status

        out["Status"] = capo_textract.types.adapter_version_status.serialize_cbor(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_cbor(data: dict) -> AdapterVersionOverview:
    out: AdapterVersionOverview = {}  # type: ignore[typeddict-item]
    if data.get("AdapterId") is not None:
        out["adapter_id"] = data["AdapterId"]
    if data.get("AdapterVersion") is not None:
        out["adapter_version"] = data["AdapterVersion"]
    if data.get("CreationTime") is not None:
        import capo_textract.types.date_time

        out["creation_time"] = capo_textract.types.date_time.deserialize_cbor(
            data["CreationTime"]
        )
    if data.get("FeatureTypes") is not None:
        import capo_textract.types.feature_types

        out["feature_types"] = capo_textract.types.feature_types.deserialize_cbor(
            data["FeatureTypes"]
        )
    if data.get("Status") is not None:
        import capo_textract.types.adapter_version_status

        out["status"] = capo_textract.types.adapter_version_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out
