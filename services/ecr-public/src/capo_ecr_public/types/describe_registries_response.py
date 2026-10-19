"""Generated from Smithy shape ``com.amazonaws.ecrpublic#DescribeRegistriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.next_token
    import capo_ecr_public.types.registry_list


class DescribeRegistriesResponse(TypedDict, closed=True):
    registries: "capo_ecr_public.types.registry_list.RegistryList"
    """<p>An object that contains the details for a public registry.</p>"""
    next_token: NotRequired["capo_ecr_public.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeRepositories</code> request. If the results of a <code>DescribeRepositories</code> request exceed <code>maxResults</code>, you can use this value to retrieve the next page of results. If there are no more results, this value is <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRegistriesResponse) -> dict:
    out: dict = {}
    import capo_ecr_public.types.registry_list

    out["registries"] = capo_ecr_public.types.registry_list.serialize_aws_json_1_1(
        value["registries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRegistriesResponse:
    out: DescribeRegistriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("registries") is not None:
        import capo_ecr_public.types.registry_list

        out["registries"] = (
            capo_ecr_public.types.registry_list.deserialize_aws_json_1_1(
                data["registries"]
            )
        )
    else:
        out["registries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
