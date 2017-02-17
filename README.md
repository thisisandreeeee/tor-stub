# Sending requests with Tor

Code stubs to help with quickly getting started sending requests through Tor. You will need to install Tor before proceeding, and the relevant python libraries.
Tor is useful to mask your IP addresses when you're sending a large number of requests. The downside is that its potentially slow, and some websites do block Tor exit nodes.

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
