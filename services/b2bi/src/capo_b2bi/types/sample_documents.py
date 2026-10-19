"""Generated from Smithy shape ``com.amazonaws.b2bi#SampleDocuments``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.bucket_name
    import capo_b2bi.types.key_list


class SampleDocuments(TypedDict, closed=True):
    bucket_name: "capo_b2bi.types.bucket_name.BucketName"
    """<p>Contains the Amazon S3 bucket that is used to hold your sample documents.</p>"""
    keys: "capo_b2bi.types.key_list.KeyList"
    """<p>Contains an array of the Amazon S3 keys used to identify the location for your sample documents.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SampleDocuments) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    import capo_b2bi.types.key_list

    out["keys"] = capo_b2bi.types.key_list.serialize_aws_json_1_0(value["keys"])
    return out


def deserialize_aws_json_1_0(data: dict) -> SampleDocuments:
    out: SampleDocuments = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        out["bucket_name"] = ""
    if data.get("keys") is not None:
        import capo_b2bi.types.key_list

        out["keys"] = capo_b2bi.types.key_list.deserialize_aws_json_1_0(data["keys"])
    else:
        out["keys"] = []
    return out
