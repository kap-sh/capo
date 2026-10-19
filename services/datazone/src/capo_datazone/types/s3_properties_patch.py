"""Generated from Smithy shape ``com.amazonaws.datazone#S3PropertiesPatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.s3_access_grant_location_id
    import capo_datazone.types.s3_uri


class S3PropertiesPatch(TypedDict, closed=True):
    s3_uri: "capo_datazone.types.s3_uri.S3Uri"
    """<p>The Amazon S3 URI that's part of the Amazon S3 properties patch of a connection.</p>"""
    s3_access_grant_location_id: NotRequired[
        "capo_datazone.types.s3_access_grant_location_id.S3AccessGrantLocationId"
    ]
    """<p>The Amazon S3 Access Grant location ID that's part of the Amazon S3 properties patch of a connection.</p>"""
    register_s3_access_grant_location: NotRequired["bool"]
    """<p>Specifies whether to register the Amazon S3 Access Grant location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3PropertiesPatch) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    if "s3_access_grant_location_id" in value:
        out["s3AccessGrantLocationId"] = value["s3_access_grant_location_id"]
    if "register_s3_access_grant_location" in value:
        out["registerS3AccessGrantLocation"] = value[
            "register_s3_access_grant_location"
        ]
    return out


def deserialize_json(data: dict) -> S3PropertiesPatch:
    out: S3PropertiesPatch = {}  # type: ignore[typeddict-item]
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("s3AccessGrantLocationId") is not None:
        out["s3_access_grant_location_id"] = data["s3AccessGrantLocationId"]
    if data.get("registerS3AccessGrantLocation") is not None:
        out["register_s3_access_grant_location"] = data["registerS3AccessGrantLocation"]
    return out
