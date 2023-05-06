from functools import cached_property

from django.core.cache.backends.redis import (
    RedisCache as _RedisCache,
    RedisCacheClient as _RedisCacheClient,
)


class RedisCacheClientNew(_RedisCacheClient):
    def ttl(self, key):
        client = self.get_client(key)
        return client.ttl(key)


class RedisCache(_RedisCache):
    @cached_property
    def _cache(self):
        return RedisCacheClientNew(self._servers, **self._options)

    def ttl(self, key, version=None):
        key = self.make_and_validate_key(key, version=version)
        return self._cache.ttl(key)
