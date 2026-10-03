"""Generated from Smithy shape ``com.amazonaws.emr#ListSupportedInstanceTypesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.string


class ListSupportedInstanceTypesInput(TypedDict, closed=True):
    release_label: NotRequired["capo_emr.types.string.String"]
    """<p>The Amazon EMR release label determines the <a href="https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-app-versions-6.x.html">versions of open-source application packages</a> that Amazon EMR has installed on the cluster. Release labels are in the format <code>emr-x.x.x</code>, where x.x.x is an Amazon EMR release number such as <code>emr-6.10.0</code>. For more information about Amazon EMR releases and their included application versions and features, see the <i> <a href="https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-components.html">Amazon EMR Release Guide</a> </i>.</p>"""
    marker: NotRequired["capo_emr.types.string.String"]
    """<p>The pagination token that marks the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSupportedInstanceTypesInput) -> dict:
    out: dict = {}
    if "release_label" in value:
        out["ReleaseLabel"] = value["release_label"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSupportedInstanceTypesInput:
    out: ListSupportedInstanceTypesInput = {}  # type: ignore[typeddict-item]
    if data.get("ReleaseLabel") is not None:
        out["release_label"] = data["ReleaseLabel"]
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    return out
