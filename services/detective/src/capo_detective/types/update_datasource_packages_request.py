"""Generated from Smithy shape ``com.amazonaws.detective#UpdateDatasourcePackagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_detective.types.datasource_package_list
    import capo_detective.types.graph_arn


class UpdateDatasourcePackagesRequest(TypedDict, closed=True):
    graph_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph.</p>"""
    datasource_packages: (
        "capo_detective.types.datasource_package_list.DatasourcePackageList"
    )
    """<p>The data source package to start for the behavior graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDatasourcePackagesRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    import capo_detective.types.datasource_package_list

    out["DatasourcePackages"] = (
        capo_detective.types.datasource_package_list.serialize_json(
            value["datasource_packages"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateDatasourcePackagesRequest:
    out: UpdateDatasourcePackagesRequest = {}  # type: ignore[typeddict-item]
    if data.get("GraphArn") is not None:
        out["graph_arn"] = data["GraphArn"]
    else:
        out["graph_arn"] = ""
    if data.get("DatasourcePackages") is not None:
        import capo_detective.types.datasource_package_list

        out["datasource_packages"] = (
            capo_detective.types.datasource_package_list.deserialize_json(
                data["DatasourcePackages"]
            )
        )
    else:
        out["datasource_packages"] = []
    return out
