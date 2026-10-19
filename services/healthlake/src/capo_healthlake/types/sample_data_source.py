"""Generated from Smithy shape ``com.amazonaws.healthlake#SampleDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.sample_data_s3_uri


class SampleDataSource(TypedDict, closed=True):
    s3_uri: "capo_healthlake.types.sample_data_s3_uri.SampleDataS3Uri"
    """<p>The Amazon S3 URI of the sample data file.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SampleDataSource) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SampleDataSource:
    out: SampleDataSource = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        out["s3_uri"] = ""
    return out
