# microprediction actor examples

Hi. This is an example of a repository that makes predictions at www.microprediction.org

Here's what's up:

- Anyone can publish live data repeatedly, [like this](https://github.com/microprediction/microprediction/blob/master/feed_examples_live/traffic_live.py) say, and it
 creates a stream like [this one](https://www.microprediction.org/stream_dashboard.html?stream=electricity-load-nyiso-overall).
- Some github repos like this one, or other sceduled jobs, make regular predictions. 
- There are also some algorithms like [this guy](https://github.com/microprediction/microprediction/blob/master/crawler_examples/soshed_boa.py) that also compete to make distributional predictions of
your data feed 1 min ahead, 5 min ahead, 15 min ahead and 1 hr ahead, but insteaad run in process.  

## Why? 
Free prediction for all ! 

 - Get live prediction of public data for free (yes it really is an [api](http://api.microprediction.org/) that predicts anything)
 - See which R, Julia and Python time series approaches seem to work best, saving you from
  trying out [hundreds of packages](https://www.microprediction.com/blog/popular-timeseries-packages) from PyPI and github of uncertain quality. 
  
Here's a [first glimpse](https://www.microprediction.com/welcome) for the uninitiated, some [categories of business application](https://www.microprediction.com/welcome-3), some remarks
on why [microprediction is synomymous with AI](https://www.microprediction.com/welcome-4) due to the possibility of value function prediction, and a straightforward
[plausibility argument](https://www.microprediction.com/welcome-2) for why an open source, openly networked collection of algorithms that 
are perfectly capable of [managing each other](https://www.microprediction.com/welcome-5) will sooner or later eclipse all other modes of production
of prediction. In order to try to get this idea off the ground, there are some ongoing [competitions](https://www.microprediction.com/competitions) and developer incentives. 
    
## Video tutorials
    
Video tutorials are available at https://www.microprediction.com/python-1 to help you
get started. There's a video explanation of FitCrawler, SequentialCrawler and friends
at https://www.microprediction.com/fitcrawler.     
    
## Presentations

Presentations at Rutgers, MIT and elsewhere can be found in the [presentations](https://github.com/microprediction/micropresentations) repo. A book will be 
published by MIT Press in 2021 on the topic. There are links to video presentations in some of the [blog](https://www.microprediction.com/blog) articles. 

![](https://i.imgur.com/uwttTku.png)
 
## Actors 

This repo shows how easy it is to set up models to make predictions using Github actions. 

While a continuous process might be more suited to submission of rapidly changing
data, a scheduled job may work just fine. Furthermore, many streams are implied 
copulas that don't change too often. 

They may be a tutorial in the (Knowledge Center)[https://www.microprediction.com/knowledge-center].

### What are z-streams? 

See [An Introduction to Z-Streams](https://www.linkedin.com/pulse/short-introduction-z-streams-peter-cotton-phd/) or the
microprediction [frequently asked questions](https://www.microprediction.com/faq). Put simply, some of the
seemingly univariate time series such as [this one](https://www.microprediction.org/stream_dashboard.html?stream=z2~copula_x~copula_y~70) are
really multi-variate implied copulas. You can retrieve them in multivariate
format using the .get_lagged_copulas or .get_lagged_zvalues methods of the [MicroReader](https://github.com/microprediction/microprediction/blob/master/microprediction/reader.py). 



