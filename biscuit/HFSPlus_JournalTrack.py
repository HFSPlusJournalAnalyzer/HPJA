


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>HPJA/HFSPlus_JournalTrack.py at master · HFSPlusJournalAnalyzer/HPJA</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="HFSPlusJournalAnalyzer/HPJA" name="twitter:title" /><meta content="HPJA - HFSPlusJournalAnalyzer" name="twitter:description" /><meta content="https://avatars1.githubusercontent.com/u/10630908?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars1.githubusercontent.com/u/10630908?v=3&amp;s=400" property="og:image" /><meta content="HFSPlusJournalAnalyzer/HPJA" property="og:title" /><meta content="https://github.com/HFSPlusJournalAnalyzer/HPJA" property="og:url" /><meta content="HPJA - HFSPlusJournalAnalyzer" property="og:description" />
      <meta name="browser-stats-url" content="/_stats">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    <link rel="xhr-socket" href="/_sockets">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="7D83BD3D:0FF3:1723C1B:54DD7DA0" name="octolytics-dimension-request_id" /><meta content="9063308" name="octolytics-actor-id" /><meta content="biscuit03" name="octolytics-actor-login" /><meta content="bda193a693410a86db1459d2239b6fcc5c2f36daccee16c1496ebd507be5d4f4" name="octolytics-actor-hash" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="Zey7/XhEhydgWDFCcPoD8u0CtegdBsvU0DmECM/gnsAPMYPsrOLlUkIKDglIaASJhwJf5vyb9fCKlzSm1saoGA==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-7f7a8d43d99dce26334cc1cb3b327f57a9309f9d6f215d6f3dff77d5e0c593a3.css" media="all" rel="stylesheet" />
    <link href="https://assets-cdn.github.com/assets/github2-a8f2a7df6fdc952a46bc2ca532f6648544a4e0a803dba39a318d244baa77bbd5.css" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="b3941243dd1d2edbd89ff1829245b524">

      
  <meta name="description" content="HPJA - HFSPlusJournalAnalyzer">
  <meta name="go-import" content="github.com/HFSPlusJournalAnalyzer/HPJA git https://github.com/HFSPlusJournalAnalyzer/HPJA.git">

  <meta content="10630908" name="octolytics-dimension-user_id" /><meta content="HFSPlusJournalAnalyzer" name="octolytics-dimension-user_login" /><meta content="29588629" name="octolytics-dimension-repository_id" /><meta content="HFSPlusJournalAnalyzer/HPJA" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="29588629" name="octolytics-dimension-repository_network_root_id" /><meta content="HFSPlusJournalAnalyzer/HPJA" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/HFSPlusJournalAnalyzer/HPJA/commits/master.atom" rel="alternate" title="Recent Commits to HPJA:master" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production windows vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" ga-data-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <form accept-charset="UTF-8" action="/HFSPlusJournalAnalyzer/HPJA/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/HFSPlusJournalAnalyzer/HPJA/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <input type="text"
    class="js-site-search-field is-clearable"
    data-hotkey="s"
    name="q"
    placeholder="Search"
    data-global-scope-placeholder="Search GitHub"
    data-repo-scope-placeholder="Search"
    tabindex="1"
    autocapitalize="off">
  <div class="scope-badge">This repository</div>
</form>
      </div>
      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item explore">
          <a class="header-nav-link" href="/explore" data-ga-click="Header, go to explore, text:explore">Explore</a>
        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/blog" data-ga-click="Header, go to blog, text:blog">Blog</a>
          </li>
        <li class="header-nav-item">
          <a class="header-nav-link" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
        </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name" href="/biscuit03" data-ga-click="Header, go to profile, text:username">
      <img alt="biscuit03" class="avatar" data-user="9063308" height="20" src="https://avatars1.githubusercontent.com/u/9063308?v=3&amp;s=40" width="20" />
      <span class="css-truncate">
        <span class="css-truncate-target">biscuit03</span>
      </span>
    </a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link js-menu-target tooltipped tooltipped-s" href="#" aria-label="Create new..." data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      
<ul class="dropdown-menu">
  <li>
    <a href="/new" data-ga-click="Header, create new repository, icon:repo"><span class="octicon octicon-repo"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new" data-ga-click="Header, create new organization, icon:organization"><span class="octicon octicon-organization"></span> New organization</a>
  </li>


    <li class="dropdown-divider"></li>
    <li class="dropdown-header">
      <span title="HFSPlusJournalAnalyzer/HPJA">This repository</span>
    </li>
      <li>
        <a href="/HFSPlusJournalAnalyzer/HPJA/issues/new" data-ga-click="Header, create new issue, icon:issue"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
      <li>
        <a href="/HFSPlusJournalAnalyzer/HPJA/settings/collaboration" data-ga-click="Header, create new collaborator, icon:person"><span class="octicon octicon-person"></span> New collaborator</a>
      </li>
</ul>

    </div>
  </li>

  <li class="header-nav-item">
        <a href="/notifications" aria-label="You have no unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:read" data-hotkey="g n">
        <span class="mail-status all-read"></span>
        <span class="octicon octicon-inbox"></span>
</a>
  </li>

  <li class="header-nav-item">
    <a class="header-nav-link tooltipped tooltipped-s" href="/settings/profile" id="account_settings" aria-label="Settings" data-ga-click="Header, go to settings, icon:settings">
      <span class="octicon octicon-gear"></span>
    </a>
  </li>

  <li class="header-nav-item">
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="wEAOoYI13X48IqknTSMQOIuCaRyQq6oTCBbInaSmT6zvAD4uXAYGxayFZDUECvcF9fYC8CgyXBAUxxQLddicVw==" /></div>
      <button class="header-nav-link sign-out-button tooltipped tooltipped-s" aria-label="Sign out" data-ga-click="Header, sign out, icon:logout">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>


    
  </div>
</div>

      

        


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

  <li>
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Ht0ojzaUOF21xJb0Rk800H9NAfrn3yZb7+qvBERhAuj2ljlnfKRvZ2lgdQReC5lp9HkZkXtyA7daZVZrNcW3JA==" /></div>    <input id="repository_id" name="repository_id" type="hidden" value="29588629" />

      <div class="select-menu js-menu-container js-select-menu">
        <a class="social-count js-social-count" href="/HFSPlusJournalAnalyzer/HPJA/watchers">
          3
        </a>
        <a href="/HFSPlusJournalAnalyzer/HPJA/subscription"
          class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0" aria-haspopup="true">
          <span class="js-select-button">
            <span class="octicon octicon-eye"></span>
            Unwatch
          </span>
        </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header">
              <span class="select-menu-title">Notifications</span>
              <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
            </div>

            <div class="select-menu-list js-navigation-container" role="menu">

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_included" name="do" type="radio" value="included" />
                  <span class="select-menu-item-heading">Not watching</span>
                  <span class="description">Be notified when participating or @mentioned.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Watch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                  <span class="select-menu-item-heading">Watching</span>
                  <span class="description">Be notified of all conversations.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Unwatch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_ignore" name="do" type="radio" value="ignore" />
                  <span class="select-menu-item-heading">Ignoring</span>
                  <span class="description">Never be notified.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-mute"></span>
                    Stop ignoring
                  </span>
                </div>
              </div>

            </div>

          </div>
        </div>
      </div>
</form>

  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/HFSPlusJournalAnalyzer/HPJA/unstar" class="js-toggler-form starred js-unstar-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="F4lmx/b359mqm8c87yb81qTg+PbThTyHkoznG+cqfXa7DdxOsHt5NWyGw33IAcKa9/gYeLnNB0gGHHEXQgdsnA==" /></div>
      <button
        class="minibutton with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar HFSPlusJournalAnalyzer/HPJA">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/HFSPlusJournalAnalyzer/HPJA/stargazers">
          0
        </a>
</form>
    <form accept-charset="UTF-8" action="/HFSPlusJournalAnalyzer/HPJA/star" class="js-toggler-form unstarred js-star-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="OUYtf7tPf9Uaqvea9AKW8khtNpSBISNkXe1bLuhuo2/pkCS0op/YO2IVS3vqvhRPUhiC6p6xMeQhynXAgRMsVA==" /></div>
      <button
        class="minibutton with-count js-toggler-target"
        aria-label="Star this repository" title="Star HFSPlusJournalAnalyzer/HPJA">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/HFSPlusJournalAnalyzer/HPJA/stargazers">
          0
        </a>
</form>  </div>

  </li>

        <li>
          <a href="/HFSPlusJournalAnalyzer/HPJA/fork" class="minibutton with-count js-toggler-target tooltipped-n" title="Fork your own copy of HFSPlusJournalAnalyzer/HPJA to your account" aria-label="Fork your own copy of HFSPlusJournalAnalyzer/HPJA to your account" rel="facebox nofollow">
            <span class="octicon octicon-repo-forked"></span>
            Fork
          </a>
          <a href="/HFSPlusJournalAnalyzer/HPJA/network" class="social-count">0</a>
        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/HFSPlusJournalAnalyzer" class="url fn" itemprop="url" rel="author"><span itemprop="title">HFSPlusJournalAnalyzer</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/HFSPlusJournalAnalyzer/HPJA" class="js-current-repository" data-pjax="#js-repo-pjax-container">HPJA</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/HFSPlusJournalAnalyzer/HPJA/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/HFSPlusJournalAnalyzer/HPJA" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /HFSPlusJournalAnalyzer/HPJA">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/HFSPlusJournalAnalyzer/HPJA/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /HFSPlusJournalAnalyzer/HPJA/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
      <a href="/HFSPlusJournalAnalyzer/HPJA/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /HFSPlusJournalAnalyzer/HPJA/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>


      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/HFSPlusJournalAnalyzer/HPJA/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /HFSPlusJournalAnalyzer/HPJA/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/HFSPlusJournalAnalyzer/HPJA/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /HFSPlusJournalAnalyzer/HPJA/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/HFSPlusJournalAnalyzer/HPJA/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /HFSPlusJournalAnalyzer/HPJA/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>
  </ul>


    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Settings">
        <a href="/HFSPlusJournalAnalyzer/HPJA/settings" aria-label="Settings" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_settings /HFSPlusJournalAnalyzer/HPJA/settings">
          <span class="octicon octicon-tools"></span> <span class="full-word">Settings</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>
    </ul>
</nav>

              <div class="only-with-full-nav">
                  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/HFSPlusJournalAnalyzer/HPJA.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="git@github.com:HFSPlusJournalAnalyzer/HPJA.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/HFSPlusJournalAnalyzer/HPJA" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<p class="clone-options">You can clone with
  <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>, <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>, or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>


  <a href="github-windows://openRepo/https://github.com/HFSPlusJournalAnalyzer/HPJA" class="minibutton sidebar-button" title="Save HFSPlusJournalAnalyzer/HPJA to your computer and use it in GitHub Desktop." aria-label="Save HFSPlusJournalAnalyzer/HPJA to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>

                <a href="/HFSPlusJournalAnalyzer/HPJA/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download the contents of HFSPlusJournalAnalyzer/HPJA as a zip file"
                   title="Download the contents of HFSPlusJournalAnalyzer/HPJA as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/HFSPlusJournalAnalyzer/HPJA/blob/f229ec350ce4175a00e4497c68bbc2d404cfc7e7/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_JournalTrack.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:4382683a39c97707bae93fcce52a8aaa -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Find or create a branch…" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/HFSPlusJournalAnalyzer/HPJA/blob/master/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_JournalTrack.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="master">master</a>
            </div>
        </div>

          <form accept-charset="UTF-8" action="/HFSPlusJournalAnalyzer/HPJA/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="fTa6RG0LzN9vRx8t4BRO2rOTOVuZhCITlsaUcHvLukybYTRqDP10uGLOMNcvXGPGr7snJtMe55hTtC1a0HzFag==" /></div>
            <span class="octicon octicon-git-branch select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <span class="select-menu-item-heading">Create branch: <span class="js-new-item-name"></span></span>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master">
            <input type="hidden" name="path" id="path" value="Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_JournalTrack.py">
</form>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="button-group right">
    <a href="/HFSPlusJournalAnalyzer/HPJA/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb js-zeroclipboard-target">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/HFSPlusJournalAnalyzer/HPJA" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">HPJA</span></a></span></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/HFSPlusJournalAnalyzer/HPJA/tree/master/Working" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">Working</span></a></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/HFSPlusJournalAnalyzer/HPJA/tree/master/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217</span></a></span><span class="separator">/</span><strong class="final-path">HFSPlus_JournalTrack.py</strong>
  </div>
</div>


  <div class="commit file-history-tease">
    <div class="file-history-tease-header">
        <img alt="hyunhochoi" class="avatar" data-user="10630780" height="24" src="https://avatars0.githubusercontent.com/u/10630780?v=3&amp;s=48" width="24" />
        <span class="author"><a href="/hyunhochoi" rel="contributor">hyunhochoi</a></span>
        <time datetime="2015-02-13T03:21:59Z" is="relative-time">Feb 13, 2015</time>
        <div class="commit-title">
            <a href="/HFSPlusJournalAnalyzer/HPJA/commit/f229ec350ce4175a00e4497c68bbc2d404cfc7e7" class="message" data-pjax="true" title="2015-02-13 12:21">2015-02-13 12:21</a>
        </div>
    </div>

    <div class="participation">
      <p class="quickstat">
        <a href="#blob_contributors_box" rel="facebox">
          <strong>1</strong>
           contributor
        </a>
      </p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="hyunhochoi" data-user="10630780" height="24" src="https://avatars0.githubusercontent.com/u/10630780?v=3&amp;s=48" width="24" />
            <a href="/hyunhochoi">hyunhochoi</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
          <span>186 lines (145 sloc)</span>
          <span class="meta-divider"></span>
        <span>5.179 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
          <a href="/HFSPlusJournalAnalyzer/HPJA/raw/master/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_JournalTrack.py" class="minibutton " id="raw-url">Raw</a>
            <a href="/HFSPlusJournalAnalyzer/HPJA/blame/master/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_JournalTrack.py" class="minibutton js-update-url-with-hash">Blame</a>
          <a href="/HFSPlusJournalAnalyzer/HPJA/commits/master/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_JournalTrack.py" class="minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->

          <a class="octicon-button tooltipped tooltipped-nw"
             href="github-windows://openRepo/https://github.com/HFSPlusJournalAnalyzer/HPJA?branch=master&amp;filepath=Working%2FHFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217%2FHFSPlus_JournalTrack.py" aria-label="Open this file in GitHub for Windows">
              <span class="octicon octicon-device-desktop"></span>
          </a>

              <a class="octicon-button js-update-url-with-hash"
                 href="/HFSPlusJournalAnalyzer/HPJA/edit/master/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_JournalTrack.py"
                 aria-label="Edit this file"
                 data-method="post" rel="nofollow" data-hotkey="e"><span class="octicon octicon-pencil"></span></a>

            <a class="octicon-button danger"
               href="/HFSPlusJournalAnalyzer/HPJA/delete/master/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_JournalTrack.py"
               aria-label="Delete this file"
               data-method="post" data-test-id="delete-blob-file" rel="nofollow">
          <span class="octicon octicon-trashcan"></span>
        </a>
      </div><!-- /.actions -->
    </div>
    

  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size-8 js-file-line-container">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code js-file-line"><span class="pl-s1"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code js-file-line"><span class="pl-s1">Created on 2015. 2. 8.</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code js-file-line"><span class="pl-s1"></span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code js-file-line"><span class="pl-s1">@author: biscuit</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code js-file-line"><span class="pl-s1"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code js-file-line"><span class="pl-k">from</span> HFSPlus_ParseModule <span class="pl-k">import</span> <span class="pl-k">*</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code js-file-line"><span class="pl-st">class</span> <span class="pl-en">JournalChange</span>:</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code js-file-line">    changeType <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code js-file-line">    parAtt <span class="pl-k">=</span> <span class="pl-s1"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code js-file-line">    curAtt <span class="pl-k">=</span> <span class="pl-s1"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code js-file-line">    changeInfo <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__init__</span></span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">changeType</span>, <span class="pl-vpf">parAtt</span><span class="pl-k">=</span><span class="pl-s1"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>, <span class="pl-vpf">curAtt</span><span class="pl-k">=</span><span class="pl-s1"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>, <span class="pl-vpf">changeInfo</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code js-file-line">        typeList <span class="pl-k">=</span> [<span class="pl-s1"><span class="pl-pds">&quot;</span>Insert<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&quot;</span>Remove<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&quot;</span>Modify<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&quot;</span>Renewal<span class="pl-pds">&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code js-file-line">        infoDict <span class="pl-k">=</span> {<span class="pl-s1"><span class="pl-pds">&#39;</span>Insert<span class="pl-pds">&#39;</span></span>:objectChangeInfo, <span class="pl-s1"><span class="pl-pds">&#39;</span>Remove<span class="pl-pds">&#39;</span></span>:objectChangeInfo,</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code js-file-line">                    <span class="pl-s1"><span class="pl-pds">&#39;</span>Modify<span class="pl-pds">&#39;</span></span>:valueChangeInfo, <span class="pl-s1"><span class="pl-pds">&#39;</span>Renewal<span class="pl-pds">&#39;</span></span>:renewalChangeInfo}</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code js-file-line">        <span class="pl-v">self</span>.changeType <span class="pl-k">=</span> changeType</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code js-file-line">        <span class="pl-v">self</span>.parAtt <span class="pl-k">=</span> parAtt</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code js-file-line">        <span class="pl-v">self</span>.curAtt <span class="pl-k">=</span> curAtt</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code js-file-line">        <span class="pl-v">self</span>.changeInfo <span class="pl-k">=</span> changeInfo</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code js-file-line">        <span class="pl-k">assert</span> changeType <span class="pl-k">in</span> typeList</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code js-file-line">        <span class="pl-k">assert</span> changeInfo.<span class="pl-sv">__class__</span> <span class="pl-k">==</span> infoDict[changeType]</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code js-file-line">        </td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__str__</span></span>(<span class="pl-vpf">self</span>):</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code js-file-line">        <span class="pl-k">return</span> <span class="pl-v">self</span>.changeType<span class="pl-k">+</span> <span class="pl-s1"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-v">self</span>.parAtt <span class="pl-k">+</span> <span class="pl-s1"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-v">self</span>.curAtt <span class="pl-k">+</span> <span class="pl-s1"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-s3">str</span>(<span class="pl-v">self</span>.changeInfo)</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code js-file-line"><span class="pl-st">class</span> <span class="pl-en">valueChangeInfo</span>:</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code js-file-line">    before <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code js-file-line">    after <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code js-file-line">    diff <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__init__</span></span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">before</span>, <span class="pl-vpf">after</span>):</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code js-file-line">        <span class="pl-v">self</span>.before <span class="pl-k">=</span> before</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code js-file-line">        <span class="pl-v">self</span>.after <span class="pl-k">=</span> after</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code js-file-line">        <span class="pl-v">self</span>.diff <span class="pl-k">=</span> <span class="pl-v">self</span>.after <span class="pl-k">-</span> <span class="pl-v">self</span>.before</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code js-file-line">        </td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__str__</span></span>(<span class="pl-vpf">self</span>):</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code js-file-line">        <span class="pl-k">return</span> <span class="pl-s1"><span class="pl-pds">&quot;</span><span class="pl-c1">%d</span> -&gt; <span class="pl-c1">%d</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (<span class="pl-v">self</span>.before, <span class="pl-v">self</span>.after)</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code js-file-line">        </td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code js-file-line"><span class="pl-st">class</span> <span class="pl-en">renewalChangeInfo</span>:</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code js-file-line">    before <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code js-file-line">    after <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code js-file-line">    renewal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__init__</span></span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">before</span>, <span class="pl-vpf">after</span>):</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code js-file-line">        <span class="pl-v">self</span>.before <span class="pl-k">=</span> before</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code js-file-line">        <span class="pl-v">self</span>.after <span class="pl-k">=</span> after</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code js-file-line">        <span class="pl-k">if</span> before <span class="pl-k">!=</span> after:</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code js-file-line">            <span class="pl-v">self</span>.renewal <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__str__</span></span>(<span class="pl-vpf">self</span>):</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code js-file-line">        <span class="pl-k">return</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>renewal<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code js-file-line"><span class="pl-st">class</span> <span class="pl-en">objectChangeInfo</span>:</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code js-file-line">    <span class="pl-s3">object</span> <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code js-file-line">    absData <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__init__</span></span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">object</span>, <span class="pl-vpf">absData</span>):</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code js-file-line">        <span class="pl-v">self</span>.object <span class="pl-k">=</span> <span class="pl-s3">object</span></td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code js-file-line">        <span class="pl-v">self</span>.absData <span class="pl-k">=</span> absData</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code js-file-line">        </td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__str__</span></span>(<span class="pl-vpf">self</span>):</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code js-file-line">        <span class="pl-k">return</span> <span class="pl-v">self</span>.object.<span class="pl-sv">__class__</span>.<span class="pl-sv">__name__</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code js-file-line"><span class="pl-st">def</span> <span class="pl-en">journalTrack</span>(<span class="pl-vpf">j_parseList</span>):</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code js-file-line">    transList <span class="pl-k">=</span> j_parseList[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code js-file-line">    changeLog <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code js-file-line">    cursur <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code js-file-line">    <span class="pl-k">for</span> trans <span class="pl-k">in</span> transList:</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code js-file-line">        ch_bukket <span class="pl-k">=</span> transTrack(trans, cursur)</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code js-file-line">        changeLog.append(ch_bukket)</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code js-file-line">        </td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code js-file-line">    <span class="pl-k">return</span> changeLog</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code js-file-line"><span class="pl-st">def</span> <span class="pl-en">transTrack</span>(<span class="pl-vpf">trans</span>, <span class="pl-vpf">cursur</span>):</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code js-file-line">    blockListHeader, bi_List, data_List <span class="pl-k">=</span> trans</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code js-file-line">    changes <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code js-file-line">    <span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-s3">range</span>(blockListHeader.num_blocks<span class="pl-k">-</span><span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code js-file-line">        changes.extend(block_check(bi_List[i], data_List[i], cursur))</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code js-file-line">    <span class="pl-k">return</span> changes</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code js-file-line"><span class="pl-st">def</span> <span class="pl-en">block_check</span>(<span class="pl-vpf">b_info</span>, <span class="pl-vpf">data</span>, <span class="pl-vpf">cursur</span>):</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code js-file-line">        p_data <span class="pl-k">=</span> cursur[b_info.bnum]</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code js-file-line">    <span class="pl-k">except</span> <span class="pl-s3">KeyError</span>:</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code js-file-line">        cursur[b_info.bnum] <span class="pl-k">=</span> data</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code js-file-line">        d_chInfo <span class="pl-k">=</span> objectChangeInfo(data, <span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code js-file-line">        j_ch <span class="pl-k">=</span> JournalChange(<span class="pl-s1"><span class="pl-pds">&quot;</span>Insert<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>, <span class="pl-s3">hex</span>(b_info.bnum), d_chInfo)</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code js-file-line">        <span class="pl-k">return</span> [j_ch]</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code js-file-line">    classType <span class="pl-k">=</span> data.<span class="pl-sv">__class__</span>.<span class="pl-sv">__name__</span></td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code js-file-line">    cursur[b_info.bnum] <span class="pl-k">=</span> data</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code js-file-line">    <span class="pl-k">return</span> data_diff(p_data, data, <span class="pl-s1"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>, classType)</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code js-file-line"><span class="pl-st">def</span> <span class="pl-en">data_diff</span>(<span class="pl-vpf">original</span>, <span class="pl-vpf">changed</span>, <span class="pl-vpf">parType</span><span class="pl-k">=</span><span class="pl-s1"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>, <span class="pl-vpf">curType</span><span class="pl-k">=</span><span class="pl-s1"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code js-file-line">    <span class="pl-k">assert</span> original.<span class="pl-sv">__class__</span> <span class="pl-k">==</span> changed.<span class="pl-sv">__class__</span></td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code js-file-line">    dType <span class="pl-k">=</span> original.<span class="pl-sv">__class__</span></td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code js-file-line">    result <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code js-file-line">    <span class="pl-k">if</span> dType <span class="pl-k">in</span> [<span class="pl-s3">int</span>, <span class="pl-s3">long</span>]:</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code js-file-line">        <span class="pl-k">if</span> original <span class="pl-k">==</span> changed: <span class="pl-k">return</span> []</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code js-file-line">        <span class="pl-k">if</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>Date<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> curType:</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code js-file-line">            r_chInfo <span class="pl-k">=</span> renewalChangeInfo(original, changed)</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code js-file-line">            j_ch <span class="pl-k">=</span> JournalChange(<span class="pl-s1"><span class="pl-pds">&quot;</span>Renewal<span class="pl-pds">&quot;</span></span>, parType, curType, r_chInfo)</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code js-file-line">            v_chInfo <span class="pl-k">=</span> valueChangeInfo(original, changed)</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code js-file-line">            j_ch <span class="pl-k">=</span> JournalChange(<span class="pl-s1"><span class="pl-pds">&quot;</span>Modify<span class="pl-pds">&quot;</span></span>, parType, curType, v_chInfo)</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code js-file-line">        result.append(j_ch)</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code js-file-line">        <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code js-file-line">    <span class="pl-k">if</span> dType <span class="pl-k">in</span> [<span class="pl-s3">tuple</span>, <span class="pl-s3">list</span>]:</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code js-file-line">        <span class="pl-k">if</span> curType <span class="pl-k">==</span> <span class="pl-s1"><span class="pl-pds">&#39;</span>LeafRecList<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code js-file-line">            result.extend(compCatalog(original, changed, parType, curType))</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code js-file-line">            <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code js-file-line">        count <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code js-file-line">        <span class="pl-k">for</span> i, j <span class="pl-k">in</span> <span class="pl-s3">zip</span>(original, changed):</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code js-file-line">            result.extend(data_diff(i, j, curType, curType <span class="pl-k">+</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>_<span class="pl-c1">%d</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> count))</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code js-file-line">            count <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code js-file-line">        <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code js-file-line">    <span class="pl-k">if</span> dType <span class="pl-k">==</span> <span class="pl-s3">memoryview</span>:</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code js-file-line">        <span class="pl-k">if</span> original <span class="pl-k">==</span> changed: <span class="pl-k">return</span> []</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code js-file-line">        r_chInfo <span class="pl-k">=</span> renewalChangeInfo(original, changed)</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code js-file-line">        j_ch <span class="pl-k">=</span> JournalChange(<span class="pl-s1"><span class="pl-pds">&quot;</span>Renewal<span class="pl-pds">&quot;</span></span>, parType, curType, r_chInfo)</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code js-file-line">        result.append(j_ch)</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code js-file-line">        <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code js-file-line">    <span class="pl-k">if</span> dType <span class="pl-k">in</span> [<span class="pl-s3">unicode</span>, <span class="pl-s3">str</span>]:</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code js-file-line">        <span class="pl-k">return</span> []</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code js-file-line">    attList <span class="pl-k">=</span> original._fields</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code js-file-line">    <span class="pl-k">for</span> att <span class="pl-k">in</span> attList:</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code js-file-line">        result.extend(data_diff(<span class="pl-s3">getattr</span>(original,att), <span class="pl-s3">getattr</span>(changed, att), parType<span class="pl-k">+</span><span class="pl-s1"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span><span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>curType, att))</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code js-file-line"><span class="pl-st">def</span> <span class="pl-en">compCatalog</span>(<span class="pl-vpf">original</span>, <span class="pl-vpf">changed</span>, <span class="pl-vpf">parType</span>, <span class="pl-vpf">curType</span>):</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code js-file-line">    orgSet <span class="pl-k">=</span> <span class="pl-s3">set</span>(original)</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code js-file-line">    chgSet <span class="pl-k">=</span> <span class="pl-s3">set</span>(changed)</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code js-file-line">    insList <span class="pl-k">=</span> chgSet <span class="pl-k">-</span> orgSet</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code js-file-line">    modList <span class="pl-k">=</span> orgSet <span class="pl-k">&amp;</span> chgSet</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code js-file-line">    remList <span class="pl-k">=</span> orgSet <span class="pl-k">-</span> chgSet</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code js-file-line">    result <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code js-file-line">            </td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code js-file-line">    <span class="pl-k">for</span> i <span class="pl-k">in</span> insList:</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code js-file-line">        chInfo <span class="pl-k">=</span> objectChangeInfo(i, <span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code js-file-line">        j_ch <span class="pl-k">=</span> JournalChange(<span class="pl-s1"><span class="pl-pds">&quot;</span>Insert<span class="pl-pds">&quot;</span></span>, parType, curType, chInfo)</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code js-file-line">        result.append(j_ch)</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code js-file-line">    <span class="pl-k">for</span> r <span class="pl-k">in</span> remList:</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code js-file-line">        chInfo <span class="pl-k">=</span> objectChangeInfo(r, <span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code js-file-line">        j_ch <span class="pl-k">=</span> JournalChange(<span class="pl-s1"><span class="pl-pds">&quot;</span>Remove<span class="pl-pds">&quot;</span></span>, parType, curType, chInfo)</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code js-file-line">        result.append(j_ch)</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code js-file-line">        </td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code js-file-line">    <span class="pl-k">for</span> m <span class="pl-k">in</span> modList:</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code js-file-line">        m_org <span class="pl-k">=</span> [x <span class="pl-k">for</span> x <span class="pl-k">in</span> original <span class="pl-k">if</span> m <span class="pl-k">==</span> x][<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code js-file-line">        m_chg <span class="pl-k">=</span> [x <span class="pl-k">for</span> x <span class="pl-k">in</span> changed <span class="pl-k">if</span> m <span class="pl-k">==</span> x][<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code js-file-line">        result.extend(data_diff(m_org, m_chg, parType, curType))</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code js-file-line"><span class="pl-st">def</span> <span class="pl-en">main</span>():</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code js-file-line">    f <span class="pl-k">=</span> <span class="pl-s3">open</span>(<span class="pl-s1"><span class="pl-st">r</span><span class="pl-pds">&quot;</span>C:<span class="pl-cce">\U</span>sers<span class="pl-cce">\u</span>ser<span class="pl-c1">\D</span>esktop<span class="pl-cce">\U</span>ntitled2<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>rb<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code js-file-line">    s <span class="pl-k">=</span> f.read()</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code js-file-line">    jParseList <span class="pl-k">=</span> journalParser(s)</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code js-file-line">    jT <span class="pl-k">=</span> journalTrack(jParseList)</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code js-file-line">    g <span class="pl-k">=</span> <span class="pl-s3">open</span>(<span class="pl-s1"><span class="pl-st">r</span><span class="pl-pds">&quot;</span>C:<span class="pl-cce">\r</span>esult2<span class="pl-c1">.</span>txt<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code js-file-line">    <span class="pl-k">for</span> i <span class="pl-k">in</span> jT:</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code js-file-line">        g.write(<span class="pl-s1"><span class="pl-pds">&quot;</span>-----------<span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code js-file-line">        <span class="pl-k">for</span> j <span class="pl-k">in</span> i:</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code js-file-line">            g.write(<span class="pl-s3">str</span>(j)<span class="pl-k">+</span><span class="pl-s1"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code js-file-line">    g.close()</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code js-file-line">    f.close()</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code js-file-line">        </td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code js-file-line"><span class="pl-k">if</span> <span class="pl-sv">__name__</span> <span class="pl-k">==</span> <span class="pl-s1"><span class="pl-pds">&#39;</span>__main__<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code js-file-line">    main()</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code js-file-line">        </td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code js-file-line">    </td>
      </tr>
</table>

  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="https://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.04797s from github-fe117-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-996268c2962f947579cb9ec2908bd576591bc94b6a2db184a78e78815022ba2c.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-a7bddfcfdd35f67bb7fe4fcd1c4fb64f6b3dad6d75980b243af9e7ad1f55035f.js"></script>
      
      

  </body>
</html>

