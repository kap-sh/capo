"""Generated from Smithy shape ``com.amazonaws.panorama#ListPackageImportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.next_token
    import capo_panorama.types.package_import_job_list


class ListPackageImportJobsResponse(TypedDict, closed=True):
    package_import_jobs: (
        "capo_panorama.types.package_import_job_list.PackageImportJobList"
    )
    """<p>A list of package import jobs.</p>"""
    next_token: NotRequired["capo_panorama.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackageImportJobsResponse) -> dict:
    out: dict = {}
    import capo_panorama.types.package_import_job_list

    out["PackageImportJobs"] = (
        capo_panorama.types.package_import_job_list.serialize_json(
            value["package_import_jobs"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPackageImportJobsResponse:
    out: ListPackageImportJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("PackageImportJobs") is not None:
        import capo_panorama.types.package_import_job_list

        out["package_import_jobs"] = (
            capo_panorama.types.package_import_job_list.deserialize_json(
                data["PackageImportJobs"]
            )
        )
    else:
        out["package_import_jobs"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
