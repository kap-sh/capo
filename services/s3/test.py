import asyncio

from zapros import AsyncClient

from capo_s3 import AsyncS3Client
from capo_s3._auth._providers import AssumeRoleCredentialsProvider, CachedProvider


async def main():
    provider = CachedProvider(AssumeRoleCredentialsProvider(AsyncClient()))
    s3 = AsyncS3Client(region="us-east-1", credentials_provider=provider)
    s3.presigned_get_object("bucket", "key", 300)  # first call on the client


asyncio.run(main())
