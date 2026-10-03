"""Generated from Smithy shape ``com.amazonaws.batch#FargatePlatformConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string


class FargatePlatformConfiguration(TypedDict, closed=True):
    platform_version: NotRequired["capo_batch.types.string.String"]
    """<p>The Fargate platform version where the jobs are running. A platform version is specified only for jobs that are running on Fargate resources. If one isn't specified, the <code>LATEST</code> platform version is used by default. This uses a recent, approved version of the Fargate platform for compute resources. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate platform versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FargatePlatformConfiguration) -> dict:
    out: dict = {}
    if "platform_version" in value:
        out["platformVersion"] = value["platform_version"]
    return out


def deserialize_json(data: dict) -> FargatePlatformConfiguration:
    out: FargatePlatformConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("platformVersion") is not None:
        out["platform_version"] = data["platformVersion"]
    return out
