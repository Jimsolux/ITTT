from html.parser import HTMLParser
import time
from html.parser import HTMLParser
from html.entities import name2codepoint
import chessdotcomParser

pstring = source_code = """<span class="UserName"><a href="#">Martin Elias</a></span>"""

pos_move = """<div class="move-feedback-row-line">
                <div class="move-feedback-row-topline">
                    <span class="move-san-component move-feedback-row-san move-feedback-row-colored analysis-bestMove" board-options="[object Object]" board-is-flipped="false" fen="r1bqkbnr/pppp1ppp/2n5/3Pp3/4P3/8/PPP2PPP/RNBQKBNR b KQkq - 0 3" selected-ply="6" show-board-preview="true" move-number="4" node-limit="8" send-score-on-line-click="true">
                    <!----> 
                    <span class="move-san-highlight"><span class="move-san-san">d5</span></span> <!----></span> <div class="move-feedback-row-description move-feedback-row-colored analysis-bestMove">is best</div></div> <!----> <div class="move-feedback-row-moves"><!----> <div class="move-feedback-row-enginewrap"><!----> 
                    <div class="engine-line-component move-feedback-row-engine" move-number="4" is-expandable="false"><span class="engine-line-thinking" style="display: none;"></span> 
                    <a target="_blank" class="score-text-score" href="//support.chess.com/article/656-what-do-the-computer-evaluation-numbers-mean-like-225" style="display: none;">+1.22</a> 
                    <span class="move-san-component engine-line-node engine-line-clickable" move-number="4" is-expandable="false"><span class="move-san-premove">4.</span> <span class="move-san-highlight">
                    <span class="move-san-san">Nce7</span></span> <!----></span><span class="move-san-component engine-line-node engine-line-clickable" move-number="4" is-expandable="false"><!----> 
                    <span class="move-san-highlight"><span class="move-san-san">Nf3</span></span> <!----></span>
                    <span class="move-san-component engine-line-node engine-line-clickable" move-number="4" is-expandable="false">
                    <span class="move-san-premove">5.</span> <span class="move-san-highlight"><span class="move-san-san">d6</span></span> <!----></span><span class="move-san-component engine-line-node engine-line-clickable" move-number="4" is-expandable="false"><!----> 
                    <span class="move-san-highlight"><span class="move-san-san">c4</span></span> <!---->
                    </span><span class="move-san-component engine-line-node engine-line-clickable" move-number="4" is-expandable="false"><span class="move-san-premove">6.</span>
                    <span class="move-san-highlight"> 
                    <span class="move-san-san">Nf6</span> 
                    </span> <!----></span><span class="move-san-component engine-line-node engine-line-clickable" move-number="4" is-expandable="false"><!----> 
                    <span class="move-san-highlight"> <span class="move-san-san">Nc3</span> </span> <!----></span><span class="move-san-component engine-line-node engine-line-clickable" move-number="4" is-expandable="false"><span class="move-san-premove">7.
                    </span> <span class="move-san-highlight"><span class="move-san-san">Ng6</span></span><!----></span> <!----> 
                    <div class="engine-line-preview" style="left: 0px; top: 0px; display: none;">
                    <div class="" style="width: 16rem; height: 16rem; max-width: none; padding-bottom: 0px; position: relative; background: var(--color-bg-opaque) var(--theme-board-style-image) 0 0 / cover no-repeat;" move-number="4" is-expandable="false">
                    <!----> <!---->  <!----> <!----> 
                    </div></div></div></div></div></div> 
                    <a target="_blank" class="score-text-score move-feedback-row-score" href="//support.chess.com/article/656-what-do-the-computer-evaluation-numbers-mean-like-225">+1.22</a>
                    </div></div></div> <!----></div></div> <div class="play-controller-scrollable" id="scroll-container">
                    <wc-eco-opening board-id="board-play-computer" link-to-explorer="" explorer-is-clickable="" opening-is-clickable="" class="eco-opening-panel">"""


neg_move = '''<div class="move-feedback-component" board-options="[object Object]" board-is-flipped="false" selected-ply="10" show-board-preview="true" fen="rnbqk1nr/pppp1ppp/8/8/3pP3/N7/PPP2PPP/R1BQKB1R b KQkq - 1 5"><div class="move-feedback-row"><div class="move-feedback-row-component" board-options="[object Object]" board-is-flipped="false" selected-ply="10" show-board-preview="true" move-number="8" node-limit="8" send-score-on-line-click="true" fen="rnbqk1nr/pppp1ppp/8/8/3pP3/N7/PPP2PPP/R1BQKB1R b KQkq - 1 5"><div class="move-feedback-row-icon">
  <svg width="26" height="26" viewBox="0 0 18 19">
    <g id="inaccuracy">
    <path class="icon-shadow" opacity="0.3" d="M9,.5a9,9,0,1,0,9,9A9,9,0,0,0,9,.5Z"></path>
    <path class="icon-background" fill="#F7C631" d="M9,0a9,9,0,1,0,9,9A9,9,0,0,0,9,0Z"></path>
    <g class="icon-component-shadow" opacity="0.2">
      <path d="M13.66,14.8a.28.28,0,0,1,0,.13.23.23,0,0,1-.08.11.28.28,0,0,1-.11.08l-.12,0h-2l-.13,0a.27.27,0,0,1-.1-.08A.36.36,0,0,1,11,14.8V12.9a.59.59,0,0,1,0-.13.36.36,0,0,1,.07-.1l.1-.08.13,0h2a.33.33,0,0,1,.23.1.39.39,0,0,1,.08.1.28.28,0,0,1,0,.13Zm-.12-3.93a.31.31,0,0,1,0,.13.3.3,0,0,1-.07.1.3.3,0,0,1-.23.08H11.43a.31.31,0,0,1-.34-.31L10.94,4.1A.5.5,0,0,1,11,3.86l.11-.08.13,0h2.11a.35.35,0,0,1,.26.1.41.41,0,0,1,.08.24Z"></path>
      <path d="M7.65,14.82a.27.27,0,0,1,0,.12.26.26,0,0,1-.07.11l-.1.07-.13,0H5.43a.25.25,0,0,1-.12,0,.27.27,0,0,1-.1-.08.31.31,0,0,1-.09-.22V13a.36.36,0,0,1,.09-.23l.1-.07.12,0H7.32a.32.32,0,0,1,.23.09.3.3,0,0,1,.07.1.28.28,0,0,1,0,.13Zm2.2-7.17a3.1,3.1,0,0,1-.36.73A5.58,5.58,0,0,1,9,9a4.85,4.85,0,0,1-.52.49,8,8,0,0,0-.65.63,1,1,0,0,0-.27.7V11a.21.21,0,0,1,0,.12.17.17,0,0,1-.06.1.23.23,0,0,1-.1.07l-.12,0H5.53a.21.21,0,0,1-.12,0,.18.18,0,0,1-.1-.07.2.2,0,0,1-.08-.1.37.37,0,0,1,0-.12v-.35a2.68,2.68,0,0,1,.13-.84,2.91,2.91,0,0,1,.33-.66,3.38,3.38,0,0,1,.45-.55c.16-.15.33-.29.49-.42a7.84,7.84,0,0,0,.65-.64,1,1,0,0,0,.25-.67.77.77,0,0,0-.07-.34.67.67,0,0,0-.23-.27A1.16,1.16,0,0,0,6.49,6,1.61,1.61,0,0,0,6,6.11a3,3,0,0,0-.41.18,1.75,1.75,0,0,0-.29.18l-.11.09A.5.5,0,0,1,5,6.62a.31.31,0,0,1-.21-.13l-1-1.21a.3.3,0,0,1,0-.4A1.36,1.36,0,0,1,4,4.68a3.07,3.07,0,0,1,.56-.38,5.49,5.49,0,0,1,.9-.37,3.69,3.69,0,0,1,1.19-.17,3.92,3.92,0,0,1,2.3.75,2.85,2.85,0,0,1,.77.92A2.82,2.82,0,0,1,10,6.71,3,3,0,0,1,9.85,7.65Z"></path>
    </g>
    <g>
      <path class="icon-component" fill="#fff" d="M13.66,14.3a.28.28,0,0,1,0,.13.23.23,0,0,1-.08.11.28.28,0,0,1-.11.08l-.12,0h-2l-.13,0a.27.27,0,0,1-.1-.08A.36.36,0,0,1,11,14.3V12.4a.59.59,0,0,1,0-.13.36.36,0,0,1,.07-.1l.1-.08.13,0h2a.33.33,0,0,1,.23.1.39.39,0,0,1,.08.1.28.28,0,0,1,0,.13Zm-.12-3.93a.31.31,0,0,1,0,.13.3.3,0,0,1-.07.1.3.3,0,0,1-.23.08H11.43a.31.31,0,0,1-.34-.31L10.94,3.6A.5.5,0,0,1,11,3.36l.11-.08.13,0h2.11a.35.35,0,0,1,.26.1.41.41,0,0,1,.08.24Z"></path>
      <path class="icon-component" fill="#fff" d="M7.65,14.32a.27.27,0,0,1,0,.12.26.26,0,0,1-.07.11l-.1.07-.13,0H5.43a.25.25,0,0,1-.12,0,.27.27,0,0,1-.1-.08.31.31,0,0,1-.09-.22V12.49a.36.36,0,0,1,.09-.23l.1-.07.12,0H7.32a.32.32,0,0,1,.23.09.3.3,0,0,1,.07.1.28.28,0,0,1,0,.13Zm2.2-7.17a3.1,3.1,0,0,1-.36.73,5.58,5.58,0,0,1-.49.6A4.85,4.85,0,0,1,8.48,9a8,8,0,0,0-.65.63,1,1,0,0,0-.27.7v.22a.21.21,0,0,1,0,.12.17.17,0,0,1-.06.1.23.23,0,0,1-.1.07l-.12,0H5.53a.21.21,0,0,1-.12,0,.18.18,0,0,1-.1-.07.2.2,0,0,1-.08-.1.37.37,0,0,1,0-.12v-.35a2.68,2.68,0,0,1,.13-.84,2.91,2.91,0,0,1,.33-.66,3.38,3.38,0,0,1,.45-.55c.16-.15.33-.29.49-.42a7.84,7.84,0,0,0,.65-.64,1,1,0,0,0,.25-.67.77.77,0,0,0-.07-.34.67.67,0,0,0-.23-.27,1.16,1.16,0,0,0-.72-.24A1.61,1.61,0,0,0,6,5.61a3,3,0,0,0-.41.18A1.75,1.75,0,0,0,5.3,6l-.11.09A.5.5,0,0,1,5,6.12.31.31,0,0,1,4.74,6l-1-1.21a.3.3,0,0,1,0-.4A1.36,1.36,0,0,1,4,4.18a3.07,3.07,0,0,1,.56-.38,5.49,5.49,0,0,1,.9-.37,3.69,3.69,0,0,1,1.19-.17A3.92,3.92,0,0,1,8.93,4a2.85,2.85,0,0,1,.77.92A2.82,2.82,0,0,1,10,6.21,3,3,0,0,1,9.85,7.15Z"></path>
    </g>
  </g>
  </svg>
</div> <div class="move-feedback-row-line"><div class="move-feedback-row-topline"><span class="move-san-component move-feedback-row-san move-feedback-row-colored analysis-inaccuracy" board-options="[object Object]" board-is-flipped="false" selected-ply="10" show-board-preview="true" move-number="8" node-limit="8" send-score-on-line-click="true" fen="rnbqk1nr/pppp1ppp/8/8/3pP3/N7/PPP2PPP/R1BQKB1R b KQkq - 1 5"><!----> <span class="move-san-highlight"><span class="move-san-san">Na3</span></span> <!----></span> <div class="move-feedback-row-description move-feedback-row-colored analysis-inaccuracy">is an inaccuracy</div></div> <!----> <div class="move-feedback-row-moves"><!----> <!----></div></div> <a target="_blank" class="score-text-score score-text-negative move-feedback-row-score" href="//support.chess.com/article/656-what-do-the-computer-evaluation-numbers-mean-like-225">-0.10</a></div></div> <div class="move-feedback-row"><div class="move-feedback-row-component" board-options="[object Object]" board-is-flipped="false" fen="rnbqk1nr/pppp1ppp/8/8/3QP3/8/PPP2PPP/RNB1KB1R b KQkq - 0 5" selected-ply="10" show-board-preview="true" move-number="8" node-limit="8" send-score-on-line-click="true"><div class="move-feedback-row-icon">
  <svg width="26" height="26" viewBox="0 0 18 19">
    <g id="best">
    <path class="icon-shadow" opacity="0.3" d="M9,.5a9,9,0,1,0,9,9A9,9,0,0,0,9,.5Z"></path>
    <path class="icon-background" fill="#81B64C" d="M9,0a9,9,0,1,0,9,9A9,9,0,0,0,9,0Z"></path>
    <path class="icon-component-shadow" opacity="0.2" d="M9,3.43a.5.5,0,0,0-.27.08.46.46,0,0,0-.17.22L7.24,7.17l-3.68.19a.52.52,0,0,0-.26.1.53.53,0,0,0-.16.23.45.45,0,0,0,0,.28.44.44,0,0,0,.15.23l2.86,2.32-1,3.56a.45.45,0,0,0,0,.28.46.46,0,0,0,.17.22.41.41,0,0,0,.26.09.43.43,0,0,0,.27-.08l3.09-2,3.09,2a.46.46,0,0,0,.53,0,.46.46,0,0,0,.17-.22.53.53,0,0,0,0-.28l-1-3.56L14.71,8.2A.44.44,0,0,0,14.86,8a.45.45,0,0,0,0-.28.53.53,0,0,0-.16-.23.52.52,0,0,0-.26-.1l-3.68-.2L9.44,3.73a.46.46,0,0,0-.17-.22A.5.5,0,0,0,9,3.43Z"></path>
    <path class="icon-component" fill="#fff" d="M9,2.93A.5.5,0,0,0,8.73,3a.46.46,0,0,0-.17.22L7.24,6.67l-3.68.19A.52.52,0,0,0,3.3,7a.53.53,0,0,0-.16.23.45.45,0,0,0,0,.28.44.44,0,0,0,.15.23L6.15,10l-1,3.56a.45.45,0,0,0,0,.28.46.46,0,0,0,.17.22.41.41,0,0,0,.26.09.43.43,0,0,0,.27-.08l3.09-2,3.09,2a.46.46,0,0,0,.53,0,.46.46,0,0,0,.17-.22.53.53,0,0,0,0-.28l-1-3.56L14.71,7.7a.44.44,0,0,0,.15-.23.45.45,0,0,0,0-.28A.53.53,0,0,0,14.7,7a.52.52,0,0,0-.26-.1l-3.68-.2L9.44,3.23A.46.46,0,0,0,9.27,3,.5.5,0,0,0,9,2.93Z"></path>
  </g>
  </svg>
</div> <div class="move-feedback-row-line"><div class="move-feedback-row-topline"><span class="move-san-component move-feedback-row-san move-feedback-row-colored analysis-bestMove" board-options="[object Object]" board-is-flipped="false" fen="rnbqk1nr/pppp1ppp/8/8/3QP3/8/PPP2PPP/RNB1KB1R b KQkq - 0 5" selected-ply="10" show-board-preview="true" move-number="8" node-limit="8" send-score-on-line-click="true"><!----> <span class="move-san-highlight"><span class="move-san-san">Qxd4</span></span> <!----></span> <div class="move-feedback-row-description move-feedback-row-colored analysis-bestMove">is best</div></div> <!----> <div class="move-feedback-row-moves"><!----> <div class="move-feedback-row-enginewrap"><!----> <div class="engine-line-component move-feedback-row-engine" move-number="8" is-expandable="false"><span class="engine-line-thinking" style="display: none;"></span> <a target="_blank" class="score-text-score" href="//support.chess.com/article/656-what-do-the-computer-evaluation-numbers-mean-like-225" style="display: none;">+0.91</a> <span class="move-san-component engine-line-node engine-line-clickable" move-number="8" is-expandable="false"><span class="move-san-premove">6.</span> <span class="move-san-highlight"><span class="move-san-san">Qf6</span></span> <!----></span><span class="move-san-component engine-line-node engine-line-clickable" move-number="8" is-expandable="false"><!----> <span class="move-san-highlight"><span class="move-san-san">Qc5</span></span> <!----></span><span class="move-san-component engine-line-node engine-line-clickable" move-number="8" is-expandable="false"><span class="move-san-premove">7.</span> <span class="move-san-highlight"><span class="move-san-san">Nc6</span></span> <!----></span><span class="move-san-component engine-line-node engine-line-clickable" move-number="8" is-expandable="false"><!----> <span class="move-san-highlight"><span class="move-san-san">Nc3</span></span> <!----></span><span class="move-san-component engine-line-node engine-line-clickable" move-number="8" is-expandable="false"><span class="move-san-premove">8.</span> <span class="move-san-highlight"><span class="move-san-san">d6</span></span> <!----></span><span class="move-san-component engine-line-node engine-line-clickable" move-number="8" is-expandable="false"><!----> <span class="move-san-highlight"><span class="move-san-san">Qc4</span></span> <!----></span><span class="move-san-component engine-line-node engine-line-clickable" move-number="8" is-expandable="false"><span class="move-san-premove">9.</span> <span class="move-san-highlight"><span class="move-san-san">Qe7</span></span> <!----></span> <!----> <div class="engine-line-preview" style="left: 0px; top: 0px; display: none;"><div class="" style="width: 16rem; height: 16rem; max-width: none; padding-bottom: 0px; position: relative; background: var(--color-bg-opaque) var(--theme-board-style-image) 0 0 / cover no-repeat;" move-number="8" is-expandable="false"><!----> <!---->  <!----> <!----> </div></div></div></div></div></div> <a target="_blank" class="score-text-score move-feedback-row-score" href="//support.chess.com/article/656-what-do-the-computer-evaluation-numbers-mean-like-225">+0.91</a></div></div></div>'''

# loss
loss = '''
    <div class="modal-game-over-header-title modal-game-over-header-show-title">Fighter Won</div>
    <div class="modal-game-over-header-subtitle modal-game-over-header-show-subtitle">by checkmate</div>
'''



# win
win = '''
<div>
    <section class="modal-content-component modal-content-light modal-game-over-component">
        <div class="modal-game-over-header-component modal-game-over-header-white-win-or-draw">
            <div class="modal-game-over-header-title modal-game-over-header-show-title"> You Beat <br> Scanner!</div> 
            <!----> 
            <button type="button" aria-label="Close" class="modal-game-over-header-close"> <span class="icon-font-chess x modal-game-over-header-icon"> </span></button></div> <div class="modal-game-over-bg"><div class="modal-game-over-users-component" id="game-over-modal" board-class="board" show-user-popover="false"><div class="modal-game-over-users-subComponent"><div class="modal-game-over-user-component modal-game-over-users-player"><div class="modal-game-over-user-avatar-container"><div class="modal-game-over-user-avatar modal-game-over-user-white modal-game-over-user-winner modal-game-over-user-winner-active"><img alt="jheuver" class="avatar-component" src="https://www.chess.com/bundles/web/images/noavatar_l.84a92436.gif" srcset="https://www.chess.com/bundles/web/images/noavatar_l.84a92436.gif, https://www.chess.com/bundles/web/images/noavatar_l.84a92436@2x.gif 2x" width="56" height="56"> <div class="modal-game-over-user-crown modal-game-over-user-crown-active"><span class="icon-font-chess chess-crown-alt modal-game-over-user-icon"></span></div></div></div> <div class="modal-game-over-user-username">jheuver</div> <!----></div> <p class="modal-game-over-users-score">
        vs
      </p> <div class="modal-game-over-user-component modal-game-over-users-player"><div class="modal-game-over-user-avatar-container"><div class="modal-game-over-user-avatar modal-game-over-user-black"><img alt="Scanner" class="avatar-component" src="https://images.chesscomfiles.com/uploads/v1/user/360171511.dc1c60b9.200x200o.8f880722cb52.png" srcset="https://images.chesscomfiles.com/uploads/v1/user/360171511.dc1c60b9.200x200o.8f880722cb52.png, https://images.chesscomfiles.com/uploads/v1/user/360171511.dc1c60b9.200x200o.8f880722cb52@2x.png 2x" width="56" height="56"> <!----></div></div> <div class="modal-game-over-user-username">Scanner</div> <!----></div></div></div> <!----> <div class="crowns-full-component game-over-modal-crowns" data-crowns="" data-modal-crowns=""><img data-filled-crown="" alt="crown" height="16" width="16" class="crowns-full-crown crowns-full-animate" src="/bundles/web/images/color-icons/crown-shadow.svg"> <img alt="crown" height="16" width="16" class="crowns-full-crown crowns-full-grayscale" src="/bundles/web/images/color-icons/crown-shadow.svg"><img alt="crown" height="16" width="16" class="crowns-full-crown crowns-full-grayscale" src="/bundles/web/images/color-icons/crown-shadow.svg"></div> <div class="modal-game-over-buttons-component"><button class="ui_v5-button-component ui_v5-button-primary ui_v5-button-large modal-game-over-buttons-btn" type="button">Share</button> <button class="ui_v5-button-component ui_v5-button-basic ui_v5-button-small modal-game-over-buttons-btn" type="button">New Bot</button> <button class="ui_v5-button-component ui_v5-button-basic ui_v5-button-small modal-game-over-buttons-btn" type="button">Game Review</button></div>  <div class=""><div class="game-over-ad-component"><div class="game-over-ad-slot" id="gameover-1"></div> <a class="ad-upgrade-link-component game-over-ad-upgrade-link" href="/membership?c=post-game-banner" target="_blank">Remove Ads</a></div></div></div></section></div>

'''




if __name__ == "__main__":
    parser = ChessdotcomParser.ChessdotcomParser()
    while(not parser.game_over):
        parser.find_move_score = True
        parser.feed(win)
        parser.reset()
        parser.found_move_score = False
        time.sleep(1)




# Extract data from parser

