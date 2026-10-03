"""Generated from Smithy shape ``com.amazonaws.synthetics#RuntimeVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.string
    import capo_synthetics.types.timestamp


class RuntimeVersion(TypedDict, closed=True):
    version_name: NotRequired["capo_synthetics.types.string.String"]
    """<p>The name of the runtime version. For a list of valid runtime versions, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html"> Canary Runtime Versions</a>.</p>"""
    description: NotRequired["capo_synthetics.types.string.String"]
    """<p>A description of the runtime version, created by Amazon.</p>"""
    release_date: NotRequired["capo_synthetics.types.timestamp.Timestamp"]
    """<p>The date that the runtime version was released.</p>"""
    deprecation_date: NotRequired["capo_synthetics.types.timestamp.Timestamp"]
    """<p>If this runtime version is deprecated, this value is the date of deprecation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeVersion) -> dict:
    out: dict = {}
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "release_date" in value:
        import capo_synthetics.types.timestamp

        out["ReleaseDate"] = capo_synthetics.types.timestamp.serialize_json(
            value["release_date"]
        )
    if "deprecation_date" in value:
        import capo_synthetics.types.timestamp

        out["DeprecationDate"] = capo_synthetics.types.timestamp.serialize_json(
            value["deprecation_date"]
        )
    return out


def deserialize_json(data: dict) -> RuntimeVersion:
    out: RuntimeVersion = {}  # type: ignore[typeddict-item]
    if data.get("VersionName") is not None:
        out["version_name"] = data["VersionName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ReleaseDate") is not None:
        import capo_synthetics.types.timestamp

        out["release_date"] = capo_synthetics.types.timestamp.deserialize_json(
            data["ReleaseDate"]
        )
    if data.get("DeprecationDate") is not None:
        import capo_synthetics.types.timestamp

        out["deprecation_date"] = capo_synthetics.types.timestamp.deserialize_json(
            data["DeprecationDate"]
        )
    return out
