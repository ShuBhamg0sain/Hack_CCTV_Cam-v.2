import marshal, base64
exec(base64.b64decode("aW1wb3J0IHJlcXVlc3RzLHJlLG9zCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKZnJvbSBvcyBpbXBvcnQgc3lzdGVtCmZyb20gcGxhdGZvcm0gaW1wb3J0IHBsYXRmb3JtCmZyb20gdGltZSBpbXBvcnQgc2xlZXAKaW1wb3J0IG9zCnB1ayA9IHBsYXRmb3JtKClbMF0sIHBsYXRmb3JtKClbMV0sICBwbGF0Zm9ybSgpWzJdLCBwbGF0Zm9ybSgpWzNdLCBwbGF0Zm9ybSgpWzRdLCBwbGF0Zm9ybSgpWzVdLCBwbGF0Zm9ybSgpWzZdCgppZiBwdWsgPT0gKCdXJywgJ2knLCAnbicsICdkJywgJ28nLCAndycsICdzJyk6CiAgICBkZWxldCA9ICdjbHMnCiAgICBkciA9ICdcXCcKZWxzZToKICAgIGRlbGV0ID0gJ2NsZWFyJwogICAgZHIgPSAnLycKCm9zLnN5c3RlbShkZWxldCkKdGltZS5zbGVlcCgxKQoKcHJpbnQoImxvYWRpbmcgbW9kdWxlcy4uLiIpCnRpbWUuc2xlZXAoMC4wNSkKb3Muc3lzdGVtKGRlbGV0KQpwcmludCgibE9hZGluZyBtb2R1bGVzLi4uIikKdGltZS5zbGVlcCgwLjA1KQpvcy5zeXN0ZW0oZGVsZXQpCnByaW50KCJsb0FkaW5nIG1vZHVsZXMuLi4iKQp0aW1lLnNsZWVwKDAuMSkKb3Muc3lzdGVtKGRlbGV0KQpwcmludCgibG9hRGluZyBtb2R1bGVzLi4uIikKdGltZS5zbGVlcCgwLjEpCm9zLnN5c3RlbShkZWxldCkKcHJpbnQoImxvYWRJbmcgbW9kdWxlcy4uLiIpCnRpbWUuc2xlZXAoMC4xKQpvcy5zeXN0ZW0oZGVsZXQpCnByaW50KCJsb2FkaU5nIG1vZHVsZXMuLi4iKQp0aW1lLnNsZWVwKDAuMSkKb3Muc3lzdGVtKGRlbGV0KQpwcmludCgibG9hZGluRyBtb2R1bGVzLi4uIikKdGltZS5zbGVlcCgwLjEpCm9zLnN5c3RlbShkZWxldCkKcHJpbnQoImxvYWRpbmcgbW9kdWxlcy4uLiIpCnRpbWUuc2xlZXAoMC4xKQpvcy5zeXN0ZW0oZGVsZXQpCnByaW50KCJsb2FkaW5nIG1PZHVsZXMuLi4iKQp0aW1lLnNsZWVwKDAuMSkKb3Muc3lzdGVtKGRlbGV0KQpwcmludCgibG9hZGluZyBtb0R1bGVzLi4uIikKdGltZS5zbGVlcCgwLjEpCm9zLnN5c3RlbShkZWxldCkKcHJpbnQoImxvYWRpbmcgbW9kVWxlcy4uLiIpCnRpbWUuc2xlZXAoMC4xKQpvcy5zeXN0ZW0oZGVsZXQpCnByaW50KCJsb2FkaW5nIG1vZHVMZXMuLi4iKQp0aW1lLnNsZWVwKDAuMSkKb3Muc3lzdGVtKGRlbGV0KQpwcmludCgibG9hZGluZyBtb2R1bEVzLi4uIikKdGltZS5zbGVlcCgwLjEpCm9zLnN5c3RlbShkZWxldCkKcHJpbnQoImxvYWRpbmcgbW9kdWxlUy4uLiIpCnRpbWUuc2xlZXAoMC4xKQpvcy5zeXN0ZW0oZGVsZXQpCnByaW50KCJsb2FkaW5nIG1vZHVsZXMuLi4iKQp0aW1lLnNsZWVwKDAuMSkKb3Muc3lzdGVtKGRlbGV0KQpwcmludCgiTG9hZGluZyBtb2R1bGVzLi4uIikKdGltZS5zbGVlcCgwLjEpCm9zLnN5c3RlbShkZWxldCkKcHJpbnQoImxPYWRpbmcgbW9kdWxlcy4uLiIpCnRpbWUuc2xlZXAoMC4xKQpvcy5zeXN0ZW0oZGVsZXQpCnByaW50KCJsb0FkaW5nIG1vZHVsZXMuLi4iKQp0aW1lLnNsZWVwKDAuMSkKb3Muc3lzdGVtKGRlbGV0KQpwcmludCgibG9hRGluZyBtb2R1bGVzLi4uIikKdGltZS5zbGVlcCgwLjEpCm9zLnN5c3RlbShkZWxldCkKcHJpbnQoImxvYWRJbmcgbW9kdWxlcy4uLiIpCnRpbWUuc2xlZXAoMC4xKQpvcy5zeXN0ZW0oZGVsZXQpCnByaW50KCJsb2FkaU5nIG1vZHVsZXMuLi4iKQp0aW1lLnNsZWVwKDAuMSkKb3Muc3lzdGVtKGRlbGV0KQpwcmludCgibG9hZGluRyBtb2R1bGVzLi4uIikKdGltZS5zbGVlcCgwLjEpCm9zLnN5c3RlbShkZWxldCkKcHJpbnQoImxvYWRpbmcgTW9kdWxlcy4uLiIpCnRpbWUuc2xlZXAoMC4xKQpvcy5zeXN0ZW0oZGVsZXQpCnByaW50KCJsb2FkaW5nIG1PZHVsZXMuLi4iKQp0aW1lLnNsZWVwKDAuMSkKb3Muc3lzdGVtKGRlbGV0KQpwcmludCgibG9hZGluZyBtb0R1bGVzLi4uIikKdGltZS5zbGVlcCgwLjEpCm9zLnN5c3RlbShkZWxldCkKcHJpbnQoImxvYWRpbmcgbW9kVWxlcy4uLiIpCnRpbWUuc2xlZXAoMC4xKQpvcy5zeXN0ZW0oZGVsZXQpCnByaW50KCJsb2FkaW5nIG1vZHVMZXMuLi4iKQp0aW1lLnNsZWVwKDAuMSkKb3Muc3lzdGVtKGRlbGV0KQpwcmludCgibG9hZGluZyBtb2R1bEVzLi4uIikKdGltZS5zbGVlcCgwLjEpCm9zLnN5c3RlbShkZWxldCkKcHJpbnQoImxvYWRpbmcgbW9kdWxlUy4uLiIpCnRpbWUuc2xlZXAoMC4xKQpvcy5zeXN0ZW0oZGVsZXQpCnByaW50KCJsb2FkaW5nIG1vZHVsZXMuLi4iKQoKdGltZS5zbGVlcCgwLjEpCm9zLnN5c3RlbShkZWxldCkKcHJpbnQoIiIiCuKWiOKUgOKUgOKUgOKWiOKUgOKUgOKWiOKWiOKWiOKUgOKUgOKWiOKWiOKWiOKWiArilojilIDilIDilIDilojilIDilIDilojilIDilIDilIDilIDilojilIDilIDilojilogK4paI4pSA4paI4pSA4paI4pSA4pSA4paI4paI4paI4pSA4pSA4paI4paI4paI4paICuKWiOKWiOKWiOKWiOKWiOKUgOKUgOKWiOKUgOKUgOKUgOKUgOKWiOKUgOKUgOKWiOKWiArilIDilojilIDilojilIDilIDilIDilojilojilojilIDilIDilojilojilojilogKIiIiKQp0aW1lLnNsZWVwKDAuMSkKb3Muc3lzdGVtKGRlbGV0KQpwcmludCgiIiIK4paI4pSA4pSA4pSA4paI4pSA4pSA4paI4paI4paI4pSA4pSA4paI4paI4paI4paI4pSA4pSA4pSA4paI4pSA4pSA4paICuKWiOKUgOKUgOKUgOKWiOKUgOKUgOKWiOKUgOKUgOKUgOKUgOKWiOKUgOKUgOKWiOKWiOKUgOKUgOKWiOKUgOKUgOKWiArilojilIDilojilIDilojilIDilIDilojilojilojilIDilIDilojilojilojilojilIDilIDilIDilojilojilojilogK4paI4paI4paI4paI4paI4pSA4pSA4paI4pSA4pSA4pSA4pSA4paI4pSA4pSA4paI4paI4pSA4pSA4paI4pSA4pSA4paICuKUgOKWiOKUgOKWiOKUgOKUgOKUgOKWiOKWiOKWiOKUgOKUgOKWiOKWiOKWiOKWiOKUgOKUgOKUgOKWiOKUgOKUgOKWiAoiIiIpCnRpbWUuc2xlZXAoMC4xKQpvcy5zeXN0ZW0oZGVsZXQpCnByaW50KCIiIgrilojilIDilIDilIDilojilIDilIDilojilojilojilIDilIDilojilojilojilojilIDilIDilIDilojilIDilIDilojilIDilIDilojilojilojilogK4paI4pSA4pSA4pSA4paI4pSA4pSA4paI4pSA4pSA4pSA4pSA4paI4pSA4pSA4paI4paI4pSA4pSA4paI4pSA4pSA4paI4pSA4pSA4paI4pSA4pSA4paICuKWiOKUgOKWiOKUgOKWiOKUgOKUgOKWiOKWiOKWiOKUgOKUgOKWiOKWiOKWiOKWiOKUgOKUgOKUgOKWiOKWiOKWiOKWiOKUgOKUgOKWiOKWiOKWiOKWiArilojilojilojilojilojilIDilIDilojilIDilIDilIDilIDilojilIDilIDilojilojilIDilIDilojilIDilIDilojilIDilIDilojilIDilIDilogK4pSA4paI4pSA4paI4pSA4pSA4pSA4paI4paI4paI4pSA4pSA4paI4paI4paI4paI4pSA4pSA4pSA4paI4pSA4pSA4paI4pSA4pSA4paI4pSA4pSA4paICiIiIikKdGltZS5zbGVlcCgwLjEpCm9zLnN5c3RlbShkZWxldCkKcHJpbnQoIiIiCuKWiOKUgOKUgOKUgOKWiOKUgOKUgOKWiOKWiOKWiOKUgOKUgOKWiOKWiOKWiOKWiOKUgOKUgOKUgOKWiOKUgOKUgOKWiOKUgOKUgOKWiOKWiOKWiOKWiOKUgOKUgOKWiOKWiOKWiOKWiArilojilIDilIDilIDilojilIDilIDilojilIDilIDilIDilIDilojilIDilIDilojilojilIDilIDilojilIDilIDilojilIDilIDilojilIDilIDilojilIDilIDilojilIDilIDilogK4paI4pSA4paI4pSA4paI4pSA4pSA4paI4paI4paI4pSA4pSA4paI4paI4paI4paI4pSA4pSA4pSA4paI4paI4paI4paI4pSA4pSA4paI4paI4paI4paI4pSA4pSA4paICuKWiOKWiOKWiOKWiOKWiOKUgOKUgOKWiOKUgOKUgOKUgOKUgOKWiOKUgOKUgOKWiOKWiOKUgOKUgOKWiOKUgOKUgOKWiOKUgOKUgOKWiOKUgOKUgOKWiOKUgOKUgOKWiOKUgOKUgOKWiArilIDilojilIDilojilIDilIDilIDilojilojilojilIDilIDilojilojilojilojilIDilIDilIDilojilIDilIDilojilIDilIDilojilIDilIDilojilIDilIDilojilojilojilogKIiIiKQp0aW1lLnNsZWVwKDAuMSkKb3Muc3lzdGVtKGRlbGV0KQpwcmludCgiIiIK4paI4pSA4pSA4pSA4paI4pSA4pSA4paI4paI4paI4pSA4pSA4paI4paI4paI4paI4pSA4pSA4pSA4paI4pSA4pSA4paI4pSA4pSA4paI4paI4paI4paI4pSA4pSA4paI4paI4paI4paI4pSA4pSA4paI4pSA4pSA4paICuKWiOKUgOKUgOKUgOKWiOKUgOKUgOKWiOKUgOKUgOKUgOKUgOKWiOKUgOKUgOKWiOKWiOKUgOKUgOKWiOKUgOKUgOKWiOKUgOKUgOKWiOKUgOKUgOKWiOKUgOKUgOKWiOKUgOKUgOKWiOKUgOKUgOKWiOKUgOKWiArilojilIDilojilIDilojilIDilIDilojilojilojilIDilIDilojilojilojilojilIDilIDilIDilojilojilojilojilIDilIDilojilojilojilojilIDilIDilojilIDilIDilIDilIDilIDilojilogK4paI4paI4paI4paI4paI4pSA4pSA4paI4pSA4pSA4pSA4pSA4paI4pSA4pSA4paI4paI4pSA4pSA4paI4pSA4pSA4paI4pSA4pSA4paI4pSA4pSA4paI4pSA4pSA4paI4pSA4pSA4paI4pSA4pSA4paI4pSA4paICuKUgOKWiOKUgOKWiOKUgOKUgOKUgOKWiOKWiOKWiOKUgOKUgOKWiOKWiOKWiOKWiOKUgOKUgOKUgOKWiOKUgOKUgOKWiOKUgOKUgOKWiOKUgOKUgOKWiOKUgOKUgOKWiOKWiOKWiOKWiOKUgOKUgOKWiOKUgOKUgOKWiAoiIiIpCnRpbWUuc2xlZXAoMC4xKQpvcy5zeXN0ZW0oZGVsZXQpCnByaW50KCIiIgrilojilojilojilojilIDilIDilIDilojilojilIDilojilogK4paI4pSA4pSA4paI4paI4pSA4pSA4pSA4paI4paI4paICuKWiOKWiOKWiOKWiOKUgOKUgOKUgOKUgOKUgOKWiArilojilIDilIDilojilojilIDilIDilIDilIDilogK4paI4paI4paI4paI4pSA4pSA4pSA4pSA4pSA4paICuKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKWiAogICAgICAgICAgICAgICAgICAuLjo6OjohfiEhISEhOi4KICAgICAgICAgICAgICAgLnhVSFdIISEgISE/TTg4V0hYOi4KICAgICAgICAgICAgIC5YKiNNQCQhISAgIVghTSQkJCQkJFdXeDouCiAgICAgICAgICAgIDohISEhISE/SCEgOiEkISQkU0hVQkhBTSQ4WDoKICAgICAgICAgICAgISF+ICB+On4hISA6fiEkISMkJGcwc2FpbiQkOFg6CiAgICAgICAgICAgICA6IX46OiFIITwgICB+LlUkWCE/UiQkJCQkJCQkTU0hCiAgICAgICAgICAgICB+IX4hISEhfn4gLjpYVyQkJFUhIT8kJCQkJCRSTU0hCiAgICAgICAgICAgICAgITp+fn4gLjohTSJUIyQkJCRTaHVCaGFtJCQkJCQhCiAgICAgICAgICAgICAgfj9XdXhpVypgICAgYCIjJCQkJDghISEhPz8hISEKICAgICAgICAgICAgIDpYLWdNJCQkJCAgICAgICBgIlQjJFR+ITgkV1VYVX4KICAgICAgICAgICAgOiVgYXN+IyQkJG06ICAgICAgICB+IX4gPyQkJCQkJAogICAgICAgICAgIDohYC4tc2FoflQkJCQkOHh4LiAgLnhXVy0gfiIiIyMqIgogLi4uLi4gICAtfn46PGAgITohOn4/VCMkJEBAV0AqPyQkICAgICAgL2AKIFckQEBNISEhIC4hfn4gISEjIyMjIy46WFVXJFchfiBgIn46ICAgIDoKICMifn5gLjp4JWAhISAgIUg6IyMjIVdNJCQkJFRpLjogLiFXVW4rIWAKIDo6On46ISFgOlh+IC46ID9ILiF1ICIkJCRCJCQkIVc6VSFUJCRNfgogLn5+ICAgOlhAIS4tfiAgID9AIyMjIygiKiQkJFckVEgkISBgCiBXaS5+IVgkPyEtfiAgICA6ID8kJCRCJFd1KCIqKiRSTSEKICRSQGkufn4gISAgICAgOiAgIH46KFNIVUJIQU0oOmBgCiA/TVhUQFd4Ln4gICAgOiAgICAgfiIjIyokJCQkTSggICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKIiIiKQp0aW1lLnNsZWVwKDEpCm9zLnN5c3RlbShkZWxldCkKcHJpbnQoJy0tLS0tLVZlcnNpb24gMS4yLS0tLS0tXG4nKQp0aW1lLnNsZWVwKDUpCm9zLnN5c3RlbShkZWxldCkKcHJpbnQoIiIiCmZvbGxvdyBtZSBJbnN0YWdyYW0gOiAgCmh0dHBzOi8vd3d3Lmluc3RhZ3JhbS5jb20vc2h1YmhhbV9nMHNhaW4vP2hsPWVuCgotLS0tLS1WZXJzaW9uIDEuMi0tLS0tLQoiIiIpCnRpbWUuc2xlZXAoNCkKb3Muc3lzdGVtKGRlbGV0KQpwcmludCgiV2VsY29tZSB0byBjYW1lcmEtaGFjayEiKQpwcmludCgiUGxlYXNlIHNlbGVjdCBjb3VudHJ5IGZvciBoYWNrIDoiKQpwcmludCgiIiIKMS4gUnVzc2lhbiBGZWRlcmF0aW9uICAgICAgICAgICAgICAgICAgICAgICAgCjIuIFVuaXRlZCBTdGF0ZXMgICAgICAgICAgICAgICAgICAgICAgICAgICAKMy4gSmFwYW4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCjQuIENhbmFkYSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKNS4gTmV3IFplYWxhbmQgICAgICAgICAgICAgICAgICAgICAgICAgICAKNi4gVWtyYWluZSAgICAgICAgICAgICAgICAgICAgICAgCjcuIEdlcm1hbnkgICAgICAgICAgICAgICAgICAgICAgIAo4LiBBdXN0cmlhICAgICAgICAgICAgICAgICAgICAgICAKOS4gU3BhaW4gICAgICAgICAgICAgICAgICAgICAgIAoxMC4gVHVya2V5IAoxMS4gSG9uZyBLb25nCjEyLiBHcmVlY2UKMTMuIFBvcnR1Z2FsCjE0LiBTaW5nYXB1cmUKMTUuIENvbHVtYmlhCgotLS0tUHJvamVjdCBieSBTaHVCaGFtZzBzYWluLS0tLQpmb2xsb3cgbWUgSW5zdGFncmFtIDogIApodHRwczovL3d3dy5pbnN0YWdyYW0uY29tL3NodWJoYW1fZzBzYWluLz9obD1lbgotLS0tLS1WZXJzaW9uIDEuMi0tLS0tLSAgICAgICAgICAgICAgICAgICAgICAKIiIiKQpudW0gPSBpbnQoaW5wdXQoImNvdW50cnkgOiAiKSkKaWYgbnVtID09IDE6CiAgICAgICAgcHJpbnQoIlxuIikJCQogICAgICAgIG9zLnN5c3RlbShkZWxldCkKICAgICAgICB0cnk6CiAgICAgICAgICAgIGhlYWRlcnMgPSB7J1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKFgxMTsgTGludXggaTY4NjsgcnY6NjguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC82OC4wJ30gICAgICAgCiAgICAgICAgICAgIGZvciBwYWdlIGluIHJhbmdlICgwLDgyKToKCQkJCiAgICAgICAgICAgICAgICB1cmwgPSAoImh0dHBzOi8vd3d3Lmluc2VjYW0ub3JnL2VuL2J5Y291bnRyeS9SVS8/cGFnZT0iK3N0cihwYWdlKSkKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICByZXMgPSByZXF1ZXN0cy5nZXQodXJsLCBoZWFkZXJzPWhlYWRlcnMpCiAgICAgICAgICAgICAgICBmaW5kaXAgPSByZS5maW5kYWxsKCdodHRwOi8vXGQrLlxkKy5cZCsuXGQrOlxkKycsIHJlcy50ZXh0KQogICAgICAgICAgICAgICAgY291bnQgPSAwCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICBmb3IgXyBpbiBmaW5kaXA6CiAgICAgICAgICAgICAgICAgICAgIGhhc2lsID0gZmluZGlwW2NvdW50XQoKICAgICAgICAgICAgICAgICAgICAgcHJpbnQgKCJcMDMzWzE7MzdtIixoYXNpbCkKCiAgICAgICAgICAgICAgICAgICAgIGYgPSBvcGVuKCdsb2dzLnR4dCcgLCAnYScpCiAgICAgICAgICAgICAgICAgICAgIGYud3JpdGUoZid7ZmluZGlwfScgKyAnXG4nKQogICAgICAgICAgICAgICAgICAgICBmLmNsb3NlKCkKCiAgICAgICAgICAgICAgICAgICAgIGNvdW50ICs9IDEKICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgIHByaW50ICgiIikgCmlmIG51bSA9PSAyOgogICAgICAgIHByaW50KCJcbiIpCQkKICAgICAgICB0cnk6CiAgICAgICAgICAgIGhlYWRlcnMgPSB7J1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKFgxMTsgTGludXggaTY4NjsgcnY6NjguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC82OC4wJ30gICAgICAgCiAgICAgICAgICAgIGZvciBwYWdlIGluIHJhbmdlICgwLDcyMCk6CgkJCQogICAgICAgICAgICAgICAgdXJsID0gKCJodHRwczovL3d3dy5pbnNlY2FtLm9yZy9lbi9ieWNvdW50cnkvVVMvP3BhZ2U9IitzdHIocGFnZSkpCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgcmVzID0gcmVxdWVzdHMuZ2V0KHVybCwgaGVhZGVycz1oZWFkZXJzKQogICAgICAgICAgICAgICAgZmluZGlwID0gcmUuZmluZGFsbCgnaHR0cDovL1xkKy5cZCsuXGQrLlxkKzpcZCsnLCByZXMudGV4dCkKICAgICAgICAgICAgICAgIGNvdW50ID0gMAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgZm9yIF8gaW4gZmluZGlwOgogICAgICAgICAgICAgICAgICAgICBoYXNpbCA9IGZpbmRpcFtjb3VudF0KCiAgICAgICAgICAgICAgICAgICAgIHByaW50ICgiXDAzM1sxOzM3bSIsaGFzaWwpCiAgICAgICAgICAgICAgICAgICAgIGYgPSBvcGVuKCdsb2dzLnR4dCcgLCAnYScpCiAgICAgICAgICAgICAgICAgICAgIGYud3JpdGUoZid7ZmluZGlwfScgKyAnXG4nKQogICAgICAgICAgICAgICAgICAgICBmLmNsb3NlKCkKICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgY291bnQgKz0gMQogICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgcHJpbnQgKCIgIikKaWYgbnVtID09IDM6CiAgICAgICAgcHJpbnQoIlxuIikJCQogICAgICAgIHRyeToKICAgICAgICAgICAgaGVhZGVycyA9IHsnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoWDExOyBMaW51eCBpNjg2OyBydjo2OC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzY4LjAnfSAgICAgICAKICAgICAgICAgICAgZm9yIHBhZ2UgaW4gcmFuZ2UgKDAsMjMyKToKCQkJCiAgICAgICAgICAgICAgICB1cmwgPSAoImh0dHBzOi8vd3d3Lmluc2VjYW0ub3JnL2VuL2J5Y291bnRyeS9KUC8/cGFnZT0iK3N0cihwYWdlKSkKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICByZXMgPSByZXF1ZXN0cy5nZXQodXJsLCBoZWFkZXJzPWhlYWRlcnMpCiAgICAgICAgICAgICAgICBmaW5kaXAgPSByZS5maW5kYWxsKCdodHRwOi8vXGQrLlxkKy5cZCsuXGQrOlxkKycsIHJlcy50ZXh0KQogICAgICAgICAgICAgICAgY291bnQgPSAwCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICBmb3IgXyBpbiBmaW5kaXA6CiAgICAgICAgICAgICAgICAgICAgIGhhc2lsID0gZmluZGlwW2NvdW50XQoKICAgICAgICAgICAgICAgICAgICAgcHJpbnQgKCJcMDMzWzE7MzdtIixoYXNpbCkKICAgICAgICAgICAgICAgICAgICAgZiA9IG9wZW4oJ2xvZ3MudHh0JyAsICdhJykKICAgICAgICAgICAgICAgICAgICAgZi53cml0ZShmJ3tmaW5kaXB9JyArICdcbicpCiAgICAgICAgICAgICAgICAgICAgIGYuY2xvc2UoKQogICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICBjb3VudCArPSAxCiAgICAgICAgZXhjZXB0OgogICAgICAgICAgICBwcmludCAoIiAiKQppZiBudW0gPT0gNDoKICAgICAgICBwcmludCgiXG4iKQkJCiAgICAgICAgdHJ5OgogICAgICAgICAgICBoZWFkZXJzID0geydVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wIChYMTE7IExpbnV4IGk2ODY7IHJ2OjY4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvNjguMCd9ICAgICAgIAogICAgICAgICAgICBmb3IgcGFnZSBpbiByYW5nZSAoMCwzOCk6CgkJCQogICAgICAgICAgICAgICAgdXJsID0gKCJodHRwczovL3d3dy5pbnNlY2FtLm9yZy9lbi9ieWNvdW50cnkvQ0EvP3BhZ2U9IitzdHIocGFnZSkpCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgcmVzID0gcmVxdWVzdHMuZ2V0KHVybCwgaGVhZGVycz1oZWFkZXJzKQogICAgICAgICAgICAgICAgZmluZGlwID0gcmUuZmluZGFsbCgnaHR0cDovL1xkKy5cZCsuXGQrLlxkKzpcZCsnLCByZXMudGV4dCkKICAgICAgICAgICAgICAgIGNvdW50ID0gMAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgZm9yIF8gaW4gZmluZGlwOgogICAgICAgICAgICAgICAgICAgICBoYXNpbCA9IGZpbmRpcFtjb3VudF0KCiAgICAgICAgICAgICAgICAgICAgIHByaW50ICgiXDAzM1sxOzM3bSIsaGFzaWwpCiAgICAgICAgICAgICAgICAgICAgIGYgPSBvcGVuKCdsb2dzLnR4dCcgLCAnYScpCiAgICAgICAgICAgICAgICAgICAgIGYud3JpdGUoZid7ZmluZGlwfScgKyAnXG4nKQogICAgICAgICAgICAgICAgICAgICBmLmNsb3NlKCkKICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgY291bnQgKz0gMQogICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgcHJpbnQgKCIgIikgICAgICAgICAgICAgCmlmIG51bSA9PSA1OgogICAgICAgIHByaW50KCJcbiIpCQkKICAgICAgICB0cnk6CiAgICAgICAgICAgIGhlYWRlcnMgPSB7J1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKFgxMTsgTGludXggaTY4NjsgcnY6NjguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC82OC4wJ30gICAgICAgCiAgICAgICAgICAgIGZvciBwYWdlIGluIHJhbmdlICgwLDUpOgoJCQkKICAgICAgICAgICAgICAgIHVybCA9ICgiaHR0cHM6Ly93d3cuaW5zZWNhbS5vcmcvZW4vYnljb3VudHJ5L05aLz9wYWdlPSIrc3RyKHBhZ2UpKQogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHJlcyA9IHJlcXVlc3RzLmdldCh1cmwsIGhlYWRlcnM9aGVhZGVycykKICAgICAgICAgICAgICAgIGZpbmRpcCA9IHJlLmZpbmRhbGwoJ2h0dHA6Ly9cZCsuXGQrLlxkKy5cZCs6XGQrJywgcmVzLnRleHQpCiAgICAgICAgICAgICAgICBjb3VudCA9IDAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgIGZvciBfIGluIGZpbmRpcDoKICAgICAgICAgICAgICAgICAgICAgaGFzaWwgPSBmaW5kaXBbY291bnRdCgogICAgICAgICAgICAgICAgICAgICBwcmludCAoIlwwMzNbMTszN20iLGhhc2lsKQogICAgICAgICAgICAgICAgICAgICBmID0gb3BlbignbG9ncy50eHQnICwgJ2EnKQogICAgICAgICAgICAgICAgICAgICBmLndyaXRlKGYne2ZpbmRpcH0nICsgJ1xuJykKICAgICAgICAgICAgICAgICAgICAgZi5jbG9zZSgpCiAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgIGNvdW50ICs9IDEKICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgIHByaW50ICgiICIpICAgICAgICAgICAgIAppZiBudW0gPT0gNjoKICAgICAgICBwcmludCgiXG4iKQkJCiAgICAgICAgdHJ5OgogICAgICAgICAgICBoZWFkZXJzID0geydVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wIChYMTE7IExpbnV4IGk2ODY7IHJ2OjY4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvNjguMCd9ICAgICAgIAogICAgICAgICAgICBmb3IgcGFnZSBpbiByYW5nZSAoMCwyKToKCQkJCiAgICAgICAgICAgICAgICB1cmwgPSAoImh0dHBzOi8vd3d3Lmluc2VjYW0ub3JnL2VuL2J5Y291bnRyeS9VSy8/cGFnZT0iK3N0cihwYWdlKSkKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICByZXMgPSByZXF1ZXN0cy5nZXQodXJsLCBoZWFkZXJzPWhlYWRlcnMpCiAgICAgICAgICAgICAgICBmaW5kaXAgPSByZS5maW5kYWxsKCdodHRwOi8vXGQrLlxkKy5cZCsuXGQrOlxkKycsIHJlcy50ZXh0KQogICAgICAgICAgICAgICAgY291bnQgPSAwCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICBmb3IgXyBpbiBmaW5kaXA6CiAgICAgICAgICAgICAgICAgICAgIGhhc2lsID0gZmluZGlwW2NvdW50XQoKICAgICAgICAgICAgICAgICAgICAgcHJpbnQgKCJcMDMzWzE7MzdtIixoYXNpbCkKICAgICAgICAgICAgICAgICAgICAgZiA9IG9wZW4oJ2xvZ3MudHh0JyAsICdhJykKICAgICAgICAgICAgICAgICAgICAgZi53cml0ZShmJ3tmaW5kaXB9JyArICdcbicpCiAgICAgICAgICAgICAgICAgICAgIGYuY2xvc2UoKQogICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICBjb3VudCArPSAxCiAgICAgICAgZXhjZXB0OgogICAgICAgICAgICBwcmludCAoIiAiKSAKaWYgbnVtID09IDc6CiAgICAgICAgcHJpbnQoIlxuIikJCQogICAgICAgIHRyeToKICAgICAgICAgICAgaGVhZGVycyA9IHsnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoWDExOyBMaW51eCBpNjg2OyBydjo2OC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzY4LjAnfSAgICAgICAKICAgICAgICAgICAgZm9yIHBhZ2UgaW4gcmFuZ2UgKDAsMTA3KToKCQkJCiAgICAgICAgICAgICAgICB1cmwgPSAoImh0dHBzOi8vd3d3Lmluc2VjYW0ub3JnL2VuL2J5Y291bnRyeS9ERS8/cGFnZT0iK3N0cihwYWdlKSkKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICByZXMgPSByZXF1ZXN0cy5nZXQodXJsLCBoZWFkZXJzPWhlYWRlcnMpCiAgICAgICAgICAgICAgICBmaW5kaXAgPSByZS5maW5kYWxsKCdodHRwOi8vXGQrLlxkKy5cZCsuXGQrOlxkKycsIHJlcy50ZXh0KQogICAgICAgICAgICAgICAgY291bnQgPSAwCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICBmb3IgXyBpbiBmaW5kaXA6CiAgICAgICAgICAgICAgICAgICAgIGhhc2lsID0gZmluZGlwW2NvdW50XQoKICAgICAgICAgICAgICAgICAgICAgcHJpbnQgKCJcMDMzWzE7MzFtIixoYXNpbCkKICAgICAgICAgICAgICAgICAgICAgZiA9IG9wZW4oJ2xvZ3MudHh0JyAsICdhJykKICAgICAgICAgICAgICAgICAgICAgZi53cml0ZShmJ3tmaW5kaXB9JyArICdcbicpCiAgICAgICAgICAgICAgICAgICAgIGYuY2xvc2UoKQogICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICBjb3VudCArPSAxCiAgICAgICAgZXhjZXB0OgogICAgICAgICAgICBwcmludCAoIiAiKQppZiBudW0gPT0gODoKICAgICAgICBwcmludCgiXG4iKQkJCiAgICAgICAgdHJ5OgogICAgICAgICAgICBoZWFkZXJzID0geydVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wIChYMTE7IExpbnV4IGk2ODY7IHJ2OjY4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvNjguMCd9ICAgICAgIAogICAgICAgICAgICBmb3IgcGFnZSBpbiByYW5nZSAoMCw0OCk6CgkJCQogICAgICAgICAgICAgICAgdXJsID0gKCJodHRwczovL3d3dy5pbnNlY2FtLm9yZy9lbi9ieWNvdW50cnkvQVQvP3BhZ2U9IitzdHIocGFnZSkpCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgcmVzID0gcmVxdWVzdHMuZ2V0KHVybCwgaGVhZGVycz1oZWFkZXJzKQogICAgICAgICAgICAgICAgZmluZGlwID0gcmUuZmluZGFsbCgnaHR0cDovL1xkKy5cZCsuXGQrLlxkKzpcZCsnLCByZXMudGV4dCkKICAgICAgICAgICAgICAgIGNvdW50ID0gMAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgZm9yIF8gaW4gZmluZGlwOgogICAgICAgICAgICAgICAgICAgICBoYXNpbCA9IGZpbmRpcFtjb3VudF0KCiAgICAgICAgICAgICAgICAgICAgIHByaW50ICgiXDAzM1sxOzMxbSIsaGFzaWwpCiAgICAgICAgICAgICAgICAgICAgIGYgPSBvcGVuKCdsb2dzLnR4dCcgLCAnYScpCiAgICAgICAgICAgICAgICAgICAgIGYud3JpdGUoZid7ZmluZGlwfScgKyAnXG4nKQogICAgICAgICAgICAgICAgICAgICBmLmNsb3NlKCkKICAgICAgICAgICAgICAgICAgICAgY291bnQgKz0gMQogICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgcHJpbnQgKCIgIikgICAgICAgICAgIAppZiBudW0gPT0gOToKICAgICAgICBwcmludCgiXG4iKQkJCiAgICAgICAgdHJ5OgogICAgICAgICAgICBoZWFkZXJzID0geydVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wIChYMTE7IExpbnV4IGk2ODY7IHJ2OjY4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvNjguMCd9ICAgICAgIAogICAgICAgICAgICBmb3IgcGFnZSBpbiByYW5nZSAoMCwzOSk6CgkJCQogICAgICAgICAgICAgICAgdXJsID0gKCJodHRwczovL3d3dy5pbnNlY2FtLm9yZy9lbi9ieWNvdW50cnkvRVMvP3BhZ2U9IitzdHIocGFnZSkpCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgcmVzID0gcmVxdWVzdHMuZ2V0KHVybCwgaGVhZGVycz1oZWFkZXJzKQogICAgICAgICAgICAgICAgZmluZGlwID0gcmUuZmluZGFsbCgnaHR0cDovL1xkKy5cZCsuXGQrLlxkKzpcZCsnLCByZXMudGV4dCkKICAgICAgICAgICAgICAgIGNvdW50ID0gMAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgZm9yIF8gaW4gZmluZGlwOgogICAgICAgICAgICAgICAgICAgICBoYXNpbCA9IGZpbmRpcFtjb3VudF0KCiAgICAgICAgICAgICAgICAgICAgIHByaW50ICgiXDAzM1sxOzMxbSIsaGFzaWwpCiAgICAgICAgICAgICAgICAgICAgIGYgPSBvcGVuKCdsb2dzLnR4dCcgLCAnYScpCiAgICAgICAgICAgICAgICAgICAgIGYud3JpdGUoZid7ZmluZGlwfScgKyAnXG4nKQogICAgICAgICAgICAgICAgICAgICBmLmNsb3NlKCkKICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgY291bnQgKz0gMQogICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgcHJpbnQgKCIgIikgIAppZiBudW0gPT0gMTA6CiAgICAgICAgcHJpbnQoIlxuIikJCQogICAgICAgIHRyeToKICAgICAgICAgICAgaGVhZGVycyA9IHsnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoWDExOyBMaW51eCBpNjg2OyBydjo2OC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzY4LjAnfSAgICAgICAKICAgICAgICAgICAgZm9yIHBhZ2UgaW4gcmFuZ2UgKDAsNTQpOgoJCQkKICAgICAgICAgICAgICAgIHVybCA9ICgiaHR0cHM6Ly93d3cuaW5zZWNhbS5vcmcvZW4vYnljb3VudHJ5L1RSLz9wYWdlPSIrc3RyKHBhZ2UpKQogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHJlcyA9IHJlcXVlc3RzLmdldCh1cmwsIGhlYWRlcnM9aGVhZGVycykKICAgICAgICAgICAgICAgIGZpbmRpcCA9IHJlLmZpbmRhbGwoJ2h0dHA6Ly9cZCsuXGQrLlxkKy5cZCs6XGQrJywgcmVzLnRleHQpCiAgICAgICAgICAgICAgICBjb3VudCA9IDAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgIGZvciBfIGluIGZpbmRpcDoKICAgICAgICAgICAgICAgICAgICAgaGFzaWwgPSBmaW5kaXBbY291bnRdCgogICAgICAgICAgICAgICAgICAgICBwcmludCAoIlwwMzNbMTszMW0iLGhhc2lsKQogICAgICAgICAgICAgICAgICAgICBmID0gb3BlbignbG9ncy50eHQnICwgJ2EnKQogICAgICAgICAgICAgICAgICAgICBmLndyaXRlKGYne2ZpbmRpcH0nICsgJ1xuJykKICAgICAgICAgICAgICAgICAgICAgZi5jbG9zZSgpCiAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgIGNvdW50ICs9IDEKICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgIHByaW50ICgiICIpICAgICAgICAgICAgIAppZiBudW0gPT0gMTE6CiAgICAgICAgcHJpbnQoIlxuIikJCQogICAgICAgIHRyeToKICAgICAgICAgICAgaGVhZGVycyA9IHsnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoWDExOyBMaW51eCBpNjg2OyBydjo2OC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzY4LjAnfSAgICAgICAKICAgICAgICAgICAgZm9yIHBhZ2UgaW4gcmFuZ2UgKDAsNyk6CgkJCQogICAgICAgICAgICAgICAgdXJsID0gKCJodHRwczovL3d3dy5pbnNlY2FtLm9yZy9lbi9ieWNvdW50cnkvSEsvP3BhZ2U9IitzdHIocGFnZSkpCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgcmVzID0gcmVxdWVzdHMuZ2V0KHVybCwgaGVhZGVycz1oZWFkZXJzKQogICAgICAgICAgICAgICAgZmluZGlwID0gcmUuZmluZGFsbCgnaHR0cDovL1xkKy5cZCsuXGQrLlxkKzpcZCsnLCByZXMudGV4dCkKICAgICAgICAgICAgICAgIGNvdW50ID0gMAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgZm9yIF8gaW4gZmluZGlwOgogICAgICAgICAgICAgICAgICAgICBoYXNpbCA9IGZpbmRpcFtjb3VudF0KCiAgICAgICAgICAgICAgICAgICAgIHByaW50ICgiXDAzM1sxOzMxbSIsaGFzaWwpCiAgICAgICAgICAgICAgICAgICAgIGYgPSBvcGVuKCdsb2dzLnR4dCcgLCAnYScpCiAgICAgICAgICAgICAgICAgICAgIGYud3JpdGUoZid7ZmluZGlwfScgKyAnXG4nKQogICAgICAgICAgICAgICAgICAgICBmLmNsb3NlKCkKICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgY291bnQgKz0gMQogICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgcHJpbnQgKCIgIikgIAppZiBudW0gPT0gMTI6CiAgICAgICAgcHJpbnQoIlxuIikJCQogICAgICAgIHRyeToKICAgICAgICAgICAgaGVhZGVycyA9IHsnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoWDExOyBMaW51eCBpNjg2OyBydjo2OC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzY4LjAnfSAgICAgICAKICAgICAgICAgICAgZm9yIHBhZ2UgaW4gcmFuZ2UgKDAsOCk6CgkJCQogICAgICAgICAgICAgICAgdXJsID0gKCJodHRwczovL3d3dy5pbnNlY2FtLm9yZy9lbi9ieWNvdW50cnkvR1IvP3BhZ2U9IitzdHIocGFnZSkpCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgcmVzID0gcmVxdWVzdHMuZ2V0KHVybCwgaGVhZGVycz1oZWFkZXJzKQogICAgICAgICAgICAgICAgZmluZGlwID0gcmUuZmluZGFsbCgnaHR0cDovL1xkKy5cZCsuXGQrLlxkKzpcZCsnLCByZXMudGV4dCkKICAgICAgICAgICAgICAgIGNvdW50ID0gMAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgZm9yIF8gaW4gZmluZGlwOgogICAgICAgICAgICAgICAgICAgICBoYXNpbCA9IGZpbmRpcFtjb3VudF0KCiAgICAgICAgICAgICAgICAgICAgIHByaW50ICgiXDAzM1sxOzMxbSIsaGFzaWwpCiAgICAgICAgICAgICAgICAgICAgIGYgPSBvcGVuKCdsb2dzLnR4dCcgLCAnYScpCiAgICAgICAgICAgICAgICAgICAgIGYud3JpdGUoZid7ZmluZGlwfScgKyAnXG4nKQogICAgICAgICAgICAgICAgICAgICBmLmNsb3NlKCkKICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgY291bnQgKz0gMQogICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgcHJpbnQgKCIgIikgICAgICAgICAgIAppZiBudW0gPT0gMTM6CiAgICAgICAgcHJpbnQoIlxuIikJCQogICAgICAgIHRyeToKICAgICAgICAgICAgaGVhZGVycyA9IHsnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoWDExOyBMaW51eCBpNjg2OyBydjo2OC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzY4LjAnfSAgICAgICAKICAgICAgICAgICAgZm9yIHBhZ2UgaW4gcmFuZ2UgKDAsNyk6CgkJCQogICAgICAgICAgICAgICAgdXJsID0gKCJodHRwczovL3d3dy5pbnNlY2FtLm9yZy9lbi9ieWNvdW50cnkvUFQvP3BhZ2U9IitzdHIocGFnZSkpCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgcmVzID0gcmVxdWVzdHMuZ2V0KHVybCwgaGVhZGVycz1oZWFkZXJzKQogICAgICAgICAgICAgICAgZmluZGlwID0gcmUuZmluZGFsbCgnaHR0cDovL1xkKy5cZCsuXGQrLlxkKzpcZCsnLCByZXMudGV4dCkKICAgICAgICAgICAgICAgIGNvdW50ID0gMAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgZm9yIF8gaW4gZmluZGlwOgogICAgICAgICAgICAgICAgICAgICBoYXNpbCA9IGZpbmRpcFtjb3VudF0KCiAgICAgICAgICAgICAgICAgICAgIHByaW50ICgiXDAzM1sxOzMxbSIsaGFzaWwpCiAgICAgICAgICAgICAgICAgICAgIGYgPSBvcGVuKCdsb2dzLnR4dCcgLCAnYScpCiAgICAgICAgICAgICAgICAgICAgIGYud3JpdGUoZid7ZmluZGlwfScgKyAnXG4nKQogICAgICAgICAgICAgICAgICAgICBmLmNsb3NlKCkKICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgY291bnQgKz0gMQogICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgcHJpbnQgKCIgIikgICAgICAgIAppZiBudW0gPT0gMTQ6CiAgICAgICAgcHJpbnQoIlxuIikJCQogICAgICAgIHRyeToKICAgICAgICAgICAgaGVhZGVycyA9IHsnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoWDExOyBMaW51eCBpNjg2OyBydjo2OC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzY4LjAnfSAgICAgICAKICAgICAgICAgICAgZm9yIHBhZ2UgaW4gcmFuZ2UgKDAsNyk6CgkJCQogICAgICAgICAgICAgICAgdXJsID0gKCJodHRwczovL3d3dy5pbnNlY2FtLm9yZy9lbi9ieWNvdW50cnkvU0cvP3BhZ2U9IitzdHIocGFnZSkpCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgcmVzID0gcmVxdWVzdHMuZ2V0KHVybCwgaGVhZGVycz1oZWFkZXJzKQogICAgICAgICAgICAgICAgZmluZGlwID0gcmUuZmluZGFsbCgnaHR0cDovL1xkKy5cZCsuXGQrLlxkKzpcZCsnLCByZXMudGV4dCkKICAgICAgICAgICAgICAgIGNvdW50ID0gMAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgZm9yIF8gaW4gZmluZGlwOgogICAgICAgICAgICAgICAgICAgICBoYXNpbCA9IGZpbmRpcFtjb3VudF0KCiAgICAgICAgICAgICAgICAgICAgIHByaW50ICgiXDAzM1sxOzMxbSIsaGFzaWwpCiAgICAgICAgICAgICAgICAgICAgIGYgPSBvcGVuKCdsb2dzLnR4dCcgLCAnYScpCiAgICAgICAgICAgICAgICAgICAgIGYud3JpdGUoZid7ZmluZGlwfScgKyAnXG4nKQogICAgICAgICAgICAgICAgICAgICBmLmNsb3NlKCkKCiAgICAgICAgICAgICAgICAgICAgIGNvdW50ICs9IDEKICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgIHByaW50ICgiICIpICAgICAgCmlmIG51bSA9PSAxNToKICAgICAgICBwcmludCgiXG4iKQkJCiAgICAgICAgdHJ5OgogICAgICAgICAgICBoZWFkZXJzID0geydVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wIChYMTE7IExpbnV4IGk2ODY7IHJ2OjY4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvNjguMCd9ICAgICAgIAogICAgICAgICAgICBmb3IgcGFnZSBpbiByYW5nZSAoMCw2KToKCQkJCiAgICAgICAgICAgICAgICB1cmwgPSAoImh0dHBzOi8vd3d3Lmluc2VjYW0ub3JnL2VuL2J5Y291bnRyeS9DTy8/cGFnZT0iK3N0cihwYWdlKSkKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICByZXMgPSByZXF1ZXN0cy5nZXQodXJsLCBoZWFkZXJzPWhlYWRlcnMpCiAgICAgICAgICAgICAgICBmaW5kaXAgPSByZS5maW5kYWxsKCdodHRwOi8vXGQrLlxkKy5cZCsuXGQrOlxkKycsIHJlcy50ZXh0KQogICAgICAgICAgICAgICAgY291bnQgPSAwCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICBmb3IgXyBpbiBmaW5kaXA6CiAgICAgICAgICAgICAgICAgICAgIGhhc2lsID0gZmluZGlwW2NvdW50XQoKICAgICAgICAgICAgICAgICAgICAgcHJpbnQgKCJcMDMzWzE7MzFtIixoYXNpbCkKICAgICAgICAgICAgICAgICAgICAgZiA9IG9wZW4oJ2xvZ3MudHh0JyAsICdhJykKICAgICAgICAgICAgICAgICAgICAgZi53cml0ZShmJ3tmaW5kaXB9JyArICdcbicpCiAgICAgICAgICAgICAgICAgICAgIGYuY2xvc2UoKQogICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICBjb3VudCArPSAxCiAgICAgICAgZXhjZXB0OgogICAgICAgICAgICBwcmludCAoIiAiKSAKCgpwcmludCgi0JPQvtGC0L7QstC+ISDQktGB0LUg0LvQvtCz0Lgg0LHRi9C70Lgg0YHQvtGF0YDQsNC90LXQvdGLINCyINGE0LDQudC7IGxvZ3MudHh0IikKcHJpbnQoIiIiCmZvbGxvdyBtZSBJbnN0YWdyYW0gOiAgCmh0dHBzOi8vd3d3Lmluc3RhZ3JhbS5jb20vc2h1YmhhbV9nMHNhaW4vP2hsPWVuCi0tVGhhbmtzIGZvciB1c2luZyB0aGlzIHByb2dyYW1tIS0tCgotLS0tLS1WZXJzaW9uIDEuMS0tLS0tLQoiIiIpCg=="))




mport requests,re,os
import time
import sys
from os import system
from platform import platform
from time import sleep
import os
puk = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'

os.system(delet)
time.sleep(1)

print("loading modules...")
time.sleep(0.05)
os.system(delet)
print("lOading modules...")
time.sleep(0.05)
os.system(delet)
print("loAding modules...")
time.sleep(0.1)
os.system(delet)
print("loaDing modules...")
time.sleep(0.1)
os.system(delet)
print("loadIng modules...")
time.sleep(0.1)
os.system(delet)
print("loadiNg modules...")
time.sleep(0.1)
os.system(delet)
print("loadinG modules...")
time.sleep(0.1)
os.system(delet)
print("loading modules...")
time.sleep(0.1)
os.system(delet)
print("loading mOdules...")
time.sleep(0.1)
os.system(delet)
print("loading moDules...")
time.sleep(0.1)
os.system(delet)
print("loading modUles...")
time.sleep(0.1)
os.system(delet)
print("loading moduLes...")
time.sleep(0.1)
os.system(delet)
print("loading modulEs...")
time.sleep(0.1)
os.system(delet)
print("loading moduleS...")
time.sleep(0.1)
os.system(delet)
print("loading modules...")
time.sleep(0.1)
os.system(delet)
print("Loading modules...")
time.sleep(0.1)
os.system(delet)
print("lOading modules...")
time.sleep(0.1)
os.system(delet)
print("loAding modules...")
time.sleep(0.1)
os.system(delet)
print("loaDing modules...")
time.sleep(0.1)
os.system(delet)
print("loadIng modules...")
time.sleep(0.1)
os.system(delet)
print("loadiNg modules...")
time.sleep(0.1)
os.system(delet)
print("loadinG modules...")
time.sleep(0.1)
os.system(delet)
print("loading Modules...")
time.sleep(0.1)
os.system(delet)
print("loading mOdules...")
time.sleep(0.1)
os.system(delet)
print("loading moDules...")
time.sleep(0.1)
os.system(delet)
print("loading modUles...")
time.sleep(0.1)
os.system(delet)
print("loading moduLes...")
time.sleep(0.1)
os.system(delet)
print("loading modulEs...")
time.sleep(0.1)
os.system(delet)
print("loading moduleS...")
time.sleep(0.1)
os.system(delet)
print("loading modules...")

time.sleep(0.1)
os.system(delet)
print("""
█───█──███──████
█───█──█────█──██
█─█─█──███──████
█████──█────█──██
─█─█───███──████
""")
time.sleep(0.1)
os.system(delet)
print("""
█───█──███──████───█──█
█───█──█────█──██──█──█
█─█─█──███──████───████
█████──█────█──██──█──█
─█─█───███──████───█──█
""")
time.sleep(0.1)
os.system(delet)
print("""
█───█──███──████───█──█──████
█───█──█────█──██──█──█──█──█
█─█─█──███──████───████──████
█████──█────█──██──█──█──█──█
─█─█───███──████───█──█──█──█
""")
time.sleep(0.1)
os.system(delet)
print("""
█───█──███──████───█──█──████──████
█───█──█────█──██──█──█──█──█──█──█
█─█─█──███──████───████──████──█
█████──█────█──██──█──█──█──█──█──█
─█─█───███──████───█──█──█──█──████
""")
time.sleep(0.1)
os.system(delet)
print("""
█───█──███──████───█──█──████──████──█──█
█───█──█────█──██──█──█──█──█──█──█──█─█
█─█─█──███──████───████──████──█─────██
█████──█────█──██──█──█──█──█──█──█──█─█
─█─█───███──████───█──█──█──█──████──█──█
""")
time.sleep(0.1)
os.system(delet)
print("""
████───██─██
█──██───███
████─────█
█──██────█
████─────█
─────────█
                  ..::::!~!!!!!:.
               .xUHWH!! !!?M88WHX:.
             .X*#M@$!!  !X!M$$$$$$WWx:.
            :!!!!!!?H! :!$!$$SHUBHAM$8X:
            !!~  ~:~!! :~!$!#$$g0sain$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
              !:~~~ .:!M"T#$$$$ShuBham$$$$$!
              ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X-gM$$$$       `"T#$T~!8$WUXU~
            :%`as~#$$$m:        ~!~ ?$$$$$$
           :!`.-sah~T$$$$8xx.  .xWW- ~""##*"
 .....   -~~:<` !:!:~?T#$$@@W@*?$$      /`
 W$@@M!!! .!~~ !!#####.:XUW$W!~ `"~:    :
 #"~~`.:x%`!!  !H:###!WM$$$$Ti.: .!WUn+!`
 :::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
 .~~   :X@!.-~   ?@####("*$$$W$TH$! `
 Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
 $R@i.~~ !     :   ~:(SHUBHAM(:``
 ?MXT@Wx.~    :     ~"##*$$$$M(                                                                                                                                             
""")
time.sleep(1)
os.system(delet)
print('------Version 1.2------\n')
time.sleep(5)
os.system(delet)
print("""
follow me Instagram :  
https://www.instagram.com/shubham_g0sain/?hl=en

------Version 1.2------
""")
time.sleep(4)
os.system(delet)
print("Welcome to camera-hack!")
print("Please select country for hack :")
print("""
1. Russian Federation                        
2. United States                           
3. Japan                                        
4. Canada                                     
5. New Zealand                           
6. Ukraine                       
7. Germany                       
8. Austria                       
9. Spain                       
10. Turkey 
11. Hong Kong
12. Greece
13. Portugal
14. Singapure
15. Columbia

----Project by ShuBhamg0sain----
follow me Instagram :  
https://www.instagram.com/shubham_g0sain/?hl=en
------Version 1.2------                      
""")
num = int(input("country : "))
if num == 1:
        print("\n")		
        os.system(delet)
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,82):
			
                url = ("https://www.insecam.org/en/bycountry/RU/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)

                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()

                     count += 1
        except:
            print ("") 
if num == 2:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,720):
			
                url = ("https://www.insecam.org/en/bycountry/US/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")
if num == 3:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,232):
			
                url = ("https://www.insecam.org/en/bycountry/JP/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")
if num == 4:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,38):
			
                url = ("https://www.insecam.org/en/bycountry/CA/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")             
if num == 5:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,5):
			
                url = ("https://www.insecam.org/en/bycountry/NZ/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")             
if num == 6:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,2):
			
                url = ("https://www.insecam.org/en/bycountry/UK/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ") 
if num == 7:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,107):
			
                url = ("https://www.insecam.org/en/bycountry/DE/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")
if num == 8:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,48):
			
                url = ("https://www.insecam.org/en/bycountry/AT/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                     count += 1
        except:
            print (" ")           
if num == 9:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,39):
			
                url = ("https://www.insecam.org/en/bycountry/ES/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")  
if num == 10:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,54):
			
                url = ("https://www.insecam.org/en/bycountry/TR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")             
if num == 11:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,7):
			
                url = ("https://www.insecam.org/en/bycountry/HK/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")  
if num == 12:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,8):
			
                url = ("https://www.insecam.org/en/bycountry/GR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")           
if num == 13:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,7):
			
                url = ("https://www.insecam.org/en/bycountry/PT/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")        
if num == 14:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,7):
			
                url = ("https://www.insecam.org/en/bycountry/SG/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()

                     count += 1
        except:
            print (" ")      
if num == 15:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,6):
			
                url = ("https://www.insecam.org/en/bycountry/CO/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ") 


print("Готово! Все логи были сохранены в файл logs.txt")
print("""
follow me Instagram :  
https://www.instagram.com/shubham_g0sain/?hl=en
--Thanks for using this programm!--

------Version 1.1------
""")
