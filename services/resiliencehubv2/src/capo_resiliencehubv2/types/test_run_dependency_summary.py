"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunDependencySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.dependency_criticality
    import capo_resiliencehubv2.types.region_list
    import capo_resiliencehubv2.types.test_run_dependency_source
    import capo_resiliencehubv2.types.uuid


class TestRunDependencySummary(TypedDict, closed=True):
    dependency_id: NotRequired["capo_resiliencehubv2.types.uuid.Uuid"]
    """<p>The unique identifier of the dependency. Absent when the dependency was entered manually and was not part of dependency discovery.</p>"""
    dependency_name: "str"
    """<p>The name of the dependency.</p>"""
    dns_name: "str"
    """<p>The DNS name of the dependency that the test run blocked.</p>"""
    criticality: (
        "capo_resiliencehubv2.types.dependency_criticality.DependencyCriticality"
    )
    """<p>The criticality classification of the dependency when the run started. A dependency that was not discovered has the UNKNOWN criticality.</p>"""
    source: (
        "capo_resiliencehubv2.types.test_run_dependency_source.TestRunDependencySource"
    )
    """<p>The origin of the dependency. A discovered dependency was found by dependency discovery; a manual dependency was entered when the run started.</p>"""
    location: NotRequired["str"]
    """<p>The location of the dependency.</p>"""
    source_regions: NotRequired["capo_resiliencehubv2.types.region_list.RegionList"]
    """<p>The source Regions from which the dependency was detected.</p>"""
    provider: NotRequired["str"]
    """<p>The provider of the dependency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRunDependencySummary) -> dict:
    out: dict = {}
    if "dependency_id" in value:
        out["dependencyId"] = value["dependency_id"]
    out["dependencyName"] = value["dependency_name"]
    out["dnsName"] = value["dns_name"]
    import capo_resiliencehubv2.types.dependency_criticality

    out["criticality"] = (
        capo_resiliencehubv2.types.dependency_criticality.serialize_json(
            value["criticality"]
        )
    )
    import capo_resiliencehubv2.types.test_run_dependency_source

    out["source"] = (
        capo_resiliencehubv2.types.test_run_dependency_source.serialize_json(
            value["source"]
        )
    )
    if "location" in value:
        out["location"] = value["location"]
    if "source_regions" in value:
        import capo_resiliencehubv2.types.region_list

        out["sourceRegions"] = capo_resiliencehubv2.types.region_list.serialize_json(
            value["source_regions"]
        )
    if "provider" in value:
        out["provider"] = value["provider"]
    return out


def deserialize_json(data: dict) -> TestRunDependencySummary:
    out: TestRunDependencySummary = {}  # type: ignore[typeddict-item]
    if data.get("dependencyId") is not None:
        out["dependency_id"] = data["dependencyId"]
    if data.get("dependencyName") is not None:
        out["dependency_name"] = data["dependencyName"]
    else:
        out["dependency_name"] = ""
    if data.get("dnsName") is not None:
        out["dns_name"] = data["dnsName"]
    else:
        out["dns_name"] = ""
    if data.get("criticality") is not None:
        import capo_resiliencehubv2.types.dependency_criticality

        out["criticality"] = (
            capo_resiliencehubv2.types.dependency_criticality.deserialize_json(
                data["criticality"]
            )
        )
    else:
        import typing

        out["criticality"] = typing.cast(
            "capo_resiliencehubv2.types.dependency_criticality.DependencyCriticality",
            "",
        )
    if data.get("source") is not None:
        import capo_resiliencehubv2.types.test_run_dependency_source

        out["source"] = (
            capo_resiliencehubv2.types.test_run_dependency_source.deserialize_json(
                data["source"]
            )
        )
    else:
        import typing

        out["source"] = typing.cast(
            "capo_resiliencehubv2.types.test_run_dependency_source.TestRunDependencySource",
            "",
        )
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("sourceRegions") is not None:
        import capo_resiliencehubv2.types.region_list

        out["source_regions"] = capo_resiliencehubv2.types.region_list.deserialize_json(
            data["sourceRegions"]
        )
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    return out
