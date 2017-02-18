# Sending requests with Tor

Created some short code stubs to help with quickly getting started sending requests through Tor. You will need to install Tor before proceeding, and the relevant python libraries. Tor is useful to mask your IP addresses when you're sending a large number of requests. The downside is that its potentially slow, and some websites do block Tor exit nodes.

![tor samples](https://raw.githubusercontent.com/thisisandreeeee/tor-stub/master/output.png)

### Installation
```
brew install tor
pip install -r requirements.txt
```
### Run Tor before running script
```
./tor.sh
```
### Using Tor wisely
Suppose we want to geocode a bunch of IP addresses using http://freegeoip.net/json/your-ip-address, a publicly available API rate limited at 10,000 per hour. I ran a quick diagnostic and found that I was able to send **500 requests in 73.8 seconds**, which means that it will take us approximately **24.6 minutes** to hit the rate limit, assuming we are able to extrapolate our requests rate. This, as compared to the same diagnostic performed for requests sent through Tor, which would take us almost **130 minutes** to send 10,000 requests. Evidently, if we were to send our requests through Tor, we would very rarely hit the rate limit - but that's not exactly what one would term an effective solution.

Given that Tor is so much slower, how can we possibly expect to increase the speed at which we are geotagging the IP addresses? The interesting thing about Tor is that you can open multiple instances of Tor, each running on a port of its own. Each instance would be running independently of every other port, and it would only require us to run 5-6 instances of Tor for us to be sending requests at the same speed as we would without Tor. Every additional instance of Tor created thereafter will only increase our geotagging speed.
