# Crawling_Basic_1

#### Robots.txt
```
> Case 1
User-agent: *
Allow: /

// Allow access to all robots.

> Case 2
User-agent: *
Disallow: /

// It does not allow access to all robots.

> Case 3
User-agent: User-Agent
Allow: /foo/bar/

// Allow access to specific robots and specific directories.

```
#### Example
```
// daum.net
User-agent: *
Disallow: /

// naver.com
User-agent: *
Disallow: /
Allow : /$ 
```