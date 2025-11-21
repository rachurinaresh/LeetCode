import sys
import heapq
from typing import List

SatelliteId = int

class SatelliteNetwork:
    TEN = 10
    THIRTY = 30

    def __init__(self):
        self.exists = set()
        self.g = {}

    def satellite_connected(self, satellite_id: SatelliteId) -> None:
        if satellite_id in self.exists:
            return
        self.exists.add(satellite_id)
        self.g.setdefault(satellite_id, set())

    def relationship_established(self, satellite_id1: SatelliteId, satellite_id2: SatelliteId) -> None:
        if satellite_id1 not in self.exists or satellite_id2 not in self.exists:
            return
        if satellite_id1 == satellite_id2:
            return
        self.g[satellite_id1].add(satellite_id2)
        self.g[satellite_id2].add(satellite_id1)

    def message_received(self, satellite_ids: List[SatelliteId]) -> None:
        seeds = [s for s in satellite_ids if s in self.exists]
        if not seeds:
            return
        pq = []
        INF = 10**30
        recv = {u: INF for u in self.exists}

        def start(u, t, p):
            cur = t
            for v in sorted(self.g.get(u, ())):
                if v == p:
                    continue
                if recv[v] <= cur:
                    continue
                heapq.heappush(pq, (cur + self.TEN, v, u))
                cur += self.TEN

        for s in sorted(seeds):
            if recv[s] > 0:
                recv[s] = 0
                start(s, 0, None)

        while pq:
            t, v, u = heapq.heappop(pq)
            if t >= recv[v]:
                continue
            recv[v] = t
            start(v, t, u)

        out = []
        for u in self.exists:
            if recv[u] == INF:
                continue
            mx = recv[u]
            for v in self.g.get(u, ()):
                rv = recv.get(v, INF)
                if rv != INF and rv > mx:
                    mx = rv
            out.append((mx + self.THIRTY, u))
        out.sort()
        for _, uid in out:
            print(f"SatelliteReportedBack: {uid}")


def main():
    network = SatelliteNetwork()
    no_commands = input()

    for _ in range(int(no_commands)):
        try:
            line = input()
        except EOFError:
            sys.exit(0)

        parameters = line.split()
        keyword = parameters[0]
        args = [int(i) for i in parameters[1:]]

        if keyword == "SatelliteConnected":
            assert len(args) == 1
            network.satellite_connected(SatelliteId(args[0]))
        elif keyword == "RelationshipEstablished":
            assert len(args) == 2
            network.relationship_established(SatelliteId(args[0]), SatelliteId(args[1]))
        elif keyword == "MessageReceived":
            argc = args[0]
            args = [SatelliteId(i) for i in args[1:]]
            assert argc == len(args)
            network.message_received(args)
        else:
            print(f"Malformed input {keyword}", file=sys.stderr)
            sys.exit(-1)


if __name__ == "__main__":
    main()
